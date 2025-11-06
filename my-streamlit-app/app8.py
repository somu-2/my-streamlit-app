import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import io

# --- Import your custom function ---
try:
    import fun3  # expects fun3.monn(fle, pqq)
except Exception as e:
    fun3 = None
    FUN3_IMPORT_ERROR = str(e)
else:
    FUN3_IMPORT_ERROR = None

st.set_page_config(page_title="12-Lead ECG Signal compression", layout="wide")

# --- Embed logo ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

logo_base64 = get_base64_image("logo.png")

if logo_base64:
    st.markdown(
        f"""
        <div style="text-align: center; margin-top:10px;">
            <img src="data:image/png;base64,{logo_base64}" width="220"><br>
            <h2 style="font-family: 'Segoe UI', Tahoma, sans-serif; color:#0b2a5b; margin-top:6px;">
                12-Lead ECG Signal compression
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.title("12-Lead ECG Signal compression")

st.write("---")

# --- Sidebar / Control Panel ---
col_left, col_right = st.columns([1, 2])

with col_left:
    st.header("Data Upload & Controls")
    uploaded_file = st.file_uploader("Upload CSV file (.csv)", type=["csv"])

    if uploaded_file is not None:
        try:
            df_in = pd.read_csv(uploaded_file, header=None)
            fle = df_in.to_numpy()
            st.success(f"File loaded: shape {fle.shape}")
        except Exception as e:
            st.error(f"Failed to read CSV: {e}")
            fle = None
    else:
        fle = None

    st.write("### Choose pqq")
    pqq_option = st.selectbox("Select pqq value", ("1", "2", "3", "4", "5", "0", "Manual"))

    if pqq_option == "Manual":
        pqq = st.number_input("Enter manual pqq value", value=1, step=1)
    else:
        pqq = int(pqq_option)

    st.write("### Choose L1 (lead for plotting)")
    l_choices = [str(i) for i in range(1, 13)] + ["0"]
    L1_choice = st.selectbox("Select L1 (1–12 or 0)", l_choices, index=11)
    L1 = int(L1_choice)

    start = st.button("▶️ Start Compression")

# -------------------------------
# Save state so graph updates live
# -------------------------------
if "compression_result" not in st.session_state:
    st.session_state["compression_result"] = None

# --- Run compression once when button pressed ---
if start:
    if FUN3_IMPORT_ERROR:
        st.error(f"fun3 import error: {FUN3_IMPORT_ERROR}")
    elif fle is None:
        st.error("Please upload a valid CSV first.")
    else:
        with st.spinner("Running compression..."):
            try:
                result = fun3.monn(fle, pqq)
                if not isinstance(result, (list, tuple)) or len(result) < 7:
                    st.error("fun3.monn did not return 7 outputs.")
                else:
                    data, pk, er, cr, ss, recon, orgi,aw,ar4,tv = result
                    st.session_state["compression_result"] = {
                        "data": np.array(data),
                        "pk": np.array(pk),
                        "er": np.array(er),
                        "cr": cr,
                        "ss": np.array(ss),
                        "recon": np.array(recon),
                        "orgi": np.array(orgi)
                    }
                    st.success("Compression completed.")
            except Exception as e:
                st.exception(e)

# --- Retrieve stored result ---
result = st.session_state["compression_result"]

with col_right:
    st.header("Results & Plots")

    if result:
        data = result["data"]
        pk = result["pk"]
        er = result["er"]
        cr = result["cr"]
        ss = result["ss"]
        recon = result["recon"]
        orgi = result["orgi"]

        # --- Display metrics ---
        st.write("### Compression Metrics")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Compression Ratio", f"{cr}")
        with col_b:
            try:
                st.metric("PRD", f"{er[10, 0]}")
            except Exception:
                st.metric("PRD", "N/A")
        with col_c:
            try:
                st.metric("PRDN", f"{er[12, 1]}")
            except Exception:
                st.metric("PRDN", "N/A")

        st.write("---")

        # Determine t
        recon_arr = np.array(recon)
        orgi_arr = np.array(orgi)
        if recon_arr.shape[0] == 12:
            recon_arr = recon_arr.T
        if orgi_arr.shape[0] == 12:
            orgi_arr = orgi_arr.T
        t = recon_arr.shape[0]

        # Dynamic slider (auto-updates graph)
        if t >= 1000:
            plot_limit = st.slider("Plot limit", min_value=1000, max_value=t, value=1000, step=1)
        else:
            plot_limit = st.slider("Plot limit", min_value=1, max_value=t, value=t, step=1)

        # Prepare data
        data_arr = np.array(data)
        if data_arr.ndim == 1:
            data_arr = data_arr.reshape(1, -1)
        pk_arr = np.array(pk).flatten()

        # --- Plotting ---
        fig, axes = plt.subplots(3, 1, figsize=(10, 9), constrained_layout=True)

        # Subplot 1: Data 2nd row + pk markers
        axes[0].set_title("Data (2nd row) with pk markers")
        if data_arr.shape[0] >= 2:
            x_row2 = np.arange(data_arr.shape[1])
            row2 = data_arr[1, :]
            axes[0].plot(x_row2, row2, label="Data (2nd row)")
            valid_pk = [p for p in pk_arr if 0 <= p < len(row2)]
            if len(valid_pk) > 0:
                axes[0].plot(valid_pk, row2[valid_pk], "*", markersize=10, label="pk")
            axes[0].legend()
            axes[0].set_xlim(0, t)
        else:
            axes[0].text(0.5, 0.5, "Insufficient data rows", ha='center', va='center')

        # Subplot 2: orgi[L1]
        axes[1].set_title(f"Original Signal (Lead {L1})")
        if L1 > 0 and L1 <= 12:
            y_org = orgi_arr[:plot_limit, L1 - 1]
            axes[1].plot(np.arange(len(y_org)), y_org, label="orgi")
            axes[1].legend()
            axes[1].set_xlim(0, plot_limit)
        else:
            axes[1].text(0.5, 0.5, "Invalid L1", ha='center', va='center')

        # Subplot 3: recon[L1]
        axes[2].set_title(f"Reconstructed Signal (Lead {L1})")
        if L1 > 0 and L1 <= 12:
            y_rec = recon_arr[:plot_limit, L1 - 1]
            axes[2].plot(np.arange(len(y_rec)), y_rec, label="recon")
            axes[2].legend()
            axes[2].set_xlim(0, plot_limit)
        else:
            axes[2].text(0.5, 0.5, "Invalid L1", ha='center', va='center')

        st.pyplot(fig)

        # --- Download sections ---
        st.write("### Download Results")

        col_d1, col_d2, col_d3 = st.columns(3)
        with col_d1:
            ss_csv = pd.DataFrame(result["ss"]).to_csv(index=False).encode("utf-8")
            st.download_button("💾 Compressed Byte (ss)", ss_csv, "compressed_ss.csv", "text/csv")

        with col_d2:
            org_csv = pd.DataFrame(orgi_arr).to_csv(index=False).encode("utf-8")
            st.download_button("💾 Original Signal (orgi)", org_csv, "original_signal.csv", "text/csv")

        with col_d3:
            rec_csv = pd.DataFrame(recon_arr).to_csv(index=False).encode("utf-8")
            st.download_button("💾 Reconstructed Signal (recon)", rec_csv, "reconstructed_signal.csv", "text/csv")

    else:
        st.info("Upload data and run compression to visualize results.")
