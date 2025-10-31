import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Matrix Processor Web App (Interactive)")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=None)
    st.write("### ✅ Uploaded Matrix:")
    st.write(df)

    st.write("### ➕ Choose a value to add to each row result:")
    option = st.selectbox(
        "Select a value or choose manual input",
        ("10", "20", "30", "40", "Manual")
    )

    if option == "Manual":
        add_value = st.number_input("Enter your own value:", value=0.0)
    else:
        add_value = float(option)

    # --- Processing (replaceable with your own logic later) ---
    row_sum = df.sum(axis=1)
    row_sum_plus = row_sum + add_value
    result = pd.DataFrame({
        "Row_Index": np.arange(len(row_sum)),
        "Row_Sum": row_sum,
        "Row_Sum_Plus_Value": row_sum_plus
    })

    st.write("### 🧮 Resulting Column Matrix (After Addition):")
    st.write(result[["Row_Sum_Plus_Value"]])

    # --- Interactive Plotly Plot ---
    st.write("### 📈 Interactive Visualization of Row Values:")
    fig = px.line(
        result,
        x="Row_Index",
        y=["Row_Sum", "Row_Sum_Plus_Value"],
        title="Row-wise Sum (Before and After Addition)",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Row Index",
        yaxis_title="Value",
        legend_title="Legend",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Download result ---
    csv = result[["Row_Sum_Plus_Value"]].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Download Result CSV",
        data=csv,
        file_name="result_matrix.csv",
        mime="text/csv"
    )

st.caption("Upload → Choose Value → Process → Visualize → Download. You can later replace the computation block with your own logic.")
