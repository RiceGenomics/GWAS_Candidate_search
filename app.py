import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Gene Expression Viewer")

st.title("Gene Expression Viewer")

# ----------------------
# Load datasets
# ----------------------
DATA_DIR = "data"

files = [f for f in os.listdir(DATA_DIR) if f.endswith((".csv", ".xlsx"))]

dataset = st.selectbox("Select expression dataset", files)

@st.cache_data
def load_data(file):
    path = os.path.join(DATA_DIR, file)
    if file.endswith(".csv"):
        return pd.read_csv(path)
    else:
        return pd.read_excel(path)

df = load_data(dataset)

# ----------------------
# Gene input
# ----------------------
gene = st.text_input("Enter gene name")

if gene:
    if gene in df["Gene"].values:
        gene_df = df[df["Gene"] == gene].drop(columns="Gene").T
        gene_df.columns = [gene]

        st.subheader(f"Expression values: {gene}")
        st.dataframe(gene_df)

        st.line_chart(gene_df)
        st.bar_chart(gene_df)
    else:
        st.error("Gene not found in this dataset")
