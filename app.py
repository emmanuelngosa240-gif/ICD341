import streamlit as st
import numpy as np
import pandas as pd

st.title("ICD 341 Statistical Dashboard")
st.write("This dashboard demonstrates interactive statistical computing.")

# Sidebar controls for interactivity
st.sidebar.header("Data Generation Settings")
mean = st.sidebar.slider("Mean", -10.0, 10.0, 0.0)
std = st.sidebar.slider("Standard Deviation", 0.1, 5.0, 1.0)
n_samples = st.sidebar.number_input("Number of Samples", 100, 10000, 1000)

# Generate data
np.random.seed(42)
data = np.random.normal(mean, std, n_samples)
df = pd.DataFrame(data, columns=["Value"])

# Display metrics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Mean", f"{np.mean(data):.2f}")
col2.metric("Std Dev", f"{np.std(data):.2f}")
col3.metric("Max", f"{np.max(data):.2f}")

# Histogram
st.subheader("Distribution Histogram")
st.bar_chart(np.histogram(data, bins=30)[0])