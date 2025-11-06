import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Matrix Processor Web App (Enhanced Control Version)")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

# Proceed only after upload
if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    # Activation button
    if st.button("🚀 Start Operation"):
        # --- Read CSV ---
        df = pd.read_csv(uploaded_file, header=None)

        # --- Calculate and show averages ---
        row_mean = df.mean(axis=1).mean()   # overall average across rows
        col_mean = df.mean(axis=0).mean()   # overall average across columns

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="📘 Row-wise Average (Overall)", value=f"{row_mean:.3f}")
        with col2:
            st.metric(label="📗 Column-wise Average (Overall)", value=f"{col_mean:.3f}")

        # --- Value selector ---
        st.write("### ➕ Choose a value to add to each row result:")
        option = st.selectbox(
            "Select a value or choose manual input",
            ("10", "20", "30", "40", "Manual")
        )

        if option == "Manual":
            add_value = st.number_input("Enter your own value:", value=0.0)
        else:
            add_value = float(option)

        # --- Processing block ---
        row_sum = df.sum(axis=1)
        row_sum_plus = row_sum + add_value

        result = pd.DataFrame({
            "Row_Index": np.arange(len(row_sum)),
            "Row_Sum": row_sum,
            "Row_Sum_Plus_Value": row_sum_plus
        })

        # --- Slider for plot range ---
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
