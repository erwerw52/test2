
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Linear Regression with Outliers", page_icon="📈")

# --- Sidebar for User Inputs ---
st.sidebar.header("Configuration")

num_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 100, 1)
a = st.sidebar.slider("Coefficient 'a' (y = ax + b + noise)", -10.0, 10.0, -2.0, 0.1)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0, 1000, 458, 1)

# --- Data Generation and Modeling ---
@st.cache_data
def generate_and_fit(a, noise_variance, num_points):
    b = 50.0
    X = np.linspace(0, 100, num_points)
    noise_std_dev = np.sqrt(noise_variance)
    y = a * X + b + np.random.normal(0, noise_std_dev, num_points)
    df = pd.DataFrame({'X': X, 'y': y})
    model = LinearRegression()
    model.fit(df[['X']], df['y'])
    return df, model

df, model = generate_and_fit(a, noise_variance, num_points)

# --- Visualization ---
st.title("Linear Regression with Outliers")
residuals = df['y'] - model.predict(df[['X']])
df['residuals'] = residuals
df['abs_residuals'] = np.abs(residuals)

# Find top 5 outliers
outlier_indices = np.argsort(np.abs(residuals))[-5:]
outlier_mask = np.zeros(len(df), dtype=bool)
outlier_mask[outlier_indices] = True

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(df['X'][~outlier_mask], df['y'][~outlier_mask], label="Generated Data", alpha=0.5)
ax.scatter(df['X'][outlier_mask], df['y'][outlier_mask], color='purple', edgecolor='black', s=100, label="Outliers")

for i in outlier_indices:
    ax.annotate(f"Outlier {i}", (df['X'][i], df['y'][i]), textcoords="offset points", xytext=(0,10), ha='center')

ax.plot(df['X'], model.predict(df[['X']]), color='r', label="Linear Regression")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

st.pyplot(fig)

# --- Model Coefficients and Outlier Information ---
st.subheader("Model Coefficients")
st.write(f"Coefficient (a): {model.coef_[0]:.2f}")
st.write(f"Intercept (b): {model.intercept_:.2f}")

st.subheader("Top 5 Outliers")
outliers_df = df.loc[outlier_indices, ['X', 'y', 'residuals', 'abs_residuals']]
st.dataframe(outliers_df)

# --- Download Data ---
st.subheader("Download Data")
csv = df[[ 'X', 'y' ]].to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='linear_regression_data.csv',
    mime='text/csv',
)

# --- How to Use ---
with st.expander("How to Use This App"):
    st.write("""
    - **Use the sliders in the sidebar** to control the data generation parameters.
    - **The plot shows** the generated data, the linear regression line, and the top 5 outliers.
    - **The model coefficients and outlier information** are displayed below the plot.
    - **You can download the generated data** as a CSV file using the download button.
    """)
