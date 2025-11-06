import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import base64

# --- Load and center logo ---
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(f.read()).decode()

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_image("logo.png")

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{logo_base64}" width="200"><br>
        <h2 style="font-family: 'Segoe UI', sans-serif; color:#1a1a1a;">
            12-Lead ECG Data compression
         </h2>
    </div>
    """,
    unsafe_allow_html=True
)

# --- File uploader ---
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

# Proceed only after upload
if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    # --- Activation button ---
    if st.button("🚀 Start Operation"):
        # --- Read CSV ---
        df = pd.read_csv(uploaded_file, header=None)


        # --- enter sf and pqq---#

        # --- Value selector ---
        st.write("###  Choose sampling frequecy of ECG signal")
        option1 = st.selectbox(
            "Select a value or choose manual input",
            ("1000", "500", "250", "360", "Manual")
        )

        if option == "Manual":
            sf = st.number_input("Enter your own value:", value=0.0)
        else:
            sf = float(option)

        # --- Value selector ---
        st.write("###  Select Number of segment")
        option1 = st.selectbox(
            "Select a value or choose manual input",
            ("1", "2", "3", "4","0", "Manual")
        )

        if option2 == "Manual":
            pqq = st.number_input("Enter your own value:", value=0.0)
        else:
            pqq = float(option)

        
        (data,pk,er,cr,ss,recon, orgi)=fun3.monn(fle,pqq)
        





        

        # --- Calculate and show averages ---
        row_mean = cr   # overall average across rows
        col_mean = er(1,1)   # overall average across columns

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="📘 Row-wise Average (Overall)", value=f"{row_mean:.3f}")
        with col2:
            st.metric(label="📗 Column-wise Average (Overall)", value=f"{col_mean:.3f}")

        



        # --- Slider for plot range ---
        result=recon
        max_rows = len(result)
        min_slider = min(1000, max_rows)  # fallback for smaller data
        plot_limit = st.slider(
            "📏 Select Maximum Row Limit for Plot:",
            min_value=min_slider,
            max_value=max_rows,
            value=min_slider,
            step=1
        )

        # Limit the data to slider value
        plot_data = result.iloc[:plot_limit]

        # --- Interactive Plotly Plot ---
        st.write("### 📈 Interactive Visualization of Row Values:")
        fig = px.line(
            plot_data,
            x="Row_Index",
            y=["Row_Sum", "Row_Sum_Plus_Value"],
            title=f"Row-wise Sum (First {plot_limit} Rows)",
            markers=True
        )
        fig.update_layout(
            xaxis_title="Row Index",
            yaxis_title="Value",
            yaxis_range=[0, plot_data[["Row_Sum", "Row_Sum_Plus_Value"]].to_numpy().max() * 1.1],
            legend_title="Legend",
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)

        # --- Download button ---
        csv = result[["Row_Sum_Plus_Value"]].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="💾 Download Result CSV",
            data=csv,
            file_name="result_matrix.csv",
            mime="text/csv"
        )

        st.caption("Upload → Start Operation → Choose Value → Visualize → Download.")

else:
    st.info("📤 Please upload a CSV file to begin.")
