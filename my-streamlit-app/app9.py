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

    st.write("### Choose Number of Beats to compress")
    pqq_option = st.selectbox("Select that value", ("2", "1", "3", "4", "5", "0", "Manual"))

    if pqq_option == "Manual":
        pqq = st.number_input("Enter manual Beats value", value=1, step=1)
    else:
        pqq = int(pqq_option)

    st.write("### Choose L1 (lead for plotting)")
    l_choices = [str(i) for i in range(1, 13)] + ["0"]
    L1_choice = st.selectbox("Select L1 (1–12 or 0 to display all Leads)", l_choices, index=11)
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
                if not isinstance(result, (list, tuple)) or len(result) < 10:
                    st.error("fun3.monn did not return 10 outputs.")
                else:
                    data, pk, er, cr, ss, recon, orgi, aw, ar4, tv = result
                    st.session_state["compression_result"] = {
                        "data": np.array(data),
                        "pk": np.array(pk),
                        "er": np.array(er),
                        "cr": cr,
                        "ss": np.array(ss),
                        "recon": np.array(recon),
                        "orgi": np.array(orgi),
                        "aw": np.array(aw),
                        "ar4": np.array(ar4),
                        "tv": np.array(tv)
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
        aw = result["aw"]
        ar4 = result["ar4"]
        tv = result["tv"]

        # --- Display metrics ---
        qp1=np.diff(pk)
        qp2=np.mean(qp1)
        qp2=1000/qp2
        qp2=np.round((qp2*60),0)
        st.write("### Compression Metrics")
        col_a, col_b, col_c, col_g = st.columns(4)
        with col_a:
            st.metric("Compression Ratio", f"{cr}")
        with col_b:
            try:
                st.metric("PRD", f"{er[12, 0]}")
            except Exception:
                st.metric("PRD", "N/A")
        with col_c:
            try:
                st.metric("PRDN", f"{er[12, 1]}")
            except Exception:
                st.metric("PRDN", "N/A")
        with col_g:
            st.metric("Heart Rate", f"{qp2}")

        st.write("---")


        # --- Display metrics for L1 lead ---
        st.write(f"Compression Metrics (Lead {L1})")
        col_d, col_e = st.columns(2)
        with col_d:
            try:
                st.metric("PRD", f"{er[(L1-1), 0]}")
            except Exception:
                st.metric("PRD", "N/A")
        with col_e:
            try:
                st.metric("PRDN", f"{er[(L1-1), 1]}")
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

       

        # Dynamic slider (auto-updates peak graph)
        t1=len(aw)
        if t1 >= 1000:
            plot_limit1 = st.slider("Plot limit", min_value=1000, max_value=t1, value=t1, step=1)
        else:
            plot_limit1 = st.slider("Plot limit", min_value=1, max_value=t1, value=t1, step=1)


        # --- Plotting ---
        fig, axes = plt.subplots(3, 1, figsize=(10, 9), constrained_layout=True)

        # Subplot 1: aw–ar4 and t–tv (custom plot)
        axes[0].set_title("R-Peak Detection result on Lead II")
        try:
            axes[0].plot(aw, ar4, '-', color='blue')
            axes[0].plot(pk, tv, '*', color='red')
            axes[0].legend()
            axes[0].set_xlim(0, plot_limit1)
        except Exception as e:
            axes[0].text(0.5, 0.5, f"Plot error: {e}", ha='center', va='center')


         # Dynamic slider (auto-updates graph main graph)
        if t >= 1000:
            plot_limit = st.slider("Plot limit", min_value=1000, max_value=t, value=1000, step=1)
        else:
            plot_limit = st.slider("Plot limit", min_value=1, max_value=t, value=t, step=1)

        # Subplot 2: Original Signal
        axes[1].set_title(f"Original Signal (Lead {L1})")
        if L1 > 0 and L1 <= 12:
            y_org = orgi_arr[:plot_limit, L1 - 1]
            axes[1].plot(np.arange(len(y_org)), y_org, label="orgi")
            axes[1].legend()
            axes[1].set_xlim(0, plot_limit)
        elif L1 == 0:
            axes[1].set_title("All 12 Leads (Original)")
            for lead_idx in range(min(orgi_arr.shape[1], 12)):
                y_org = orgi_arr[:plot_limit, lead_idx]
                axes[1].plot(np.arange(len(y_org)), y_org, label=f"Lead {lead_idx+1}")
            axes[1].legend(fontsize='small', ncol=3)
            axes[1].set_xlim(0, plot_limit)
                    
        else:
            axes[1].text(0.5, 0.5, "Invalid L1", ha='center', va='center')

        # Subplot 3: Reconstructed Signal
        axes[2].set_title(f"Reconstructed Signal (Lead {L1})")
        if L1 > 0 and L1 <= 12:
            y_rec = recon_arr[:plot_limit, L1 - 1]
            axes[2].plot(np.arange(len(y_rec)), y_rec, label="recon")
            axes[2].legend()
            axes[2].set_xlim(0, plot_limit)
        elif L1 == 0:
            axes[2].set_title("All 12 Leads (Reconstructed)")
            for lead_idx in range(min(recon_arr.shape[1], 12)):
                y_rec = recon_arr[:plot_limit, lead_idx]
                axes[2].plot(np.arange(len(y_rec)), y_rec, label=f"Lead {lead_idx+1}")
            axes[2].legend(fontsize='small', ncol=3)
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


