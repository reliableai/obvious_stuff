import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set page title
st.title("Beta Distribution Visualization")

# Sidebar for controls
st.sidebar.header("Parameters")

# Define all sliders in the sidebar
Nr = st.sidebar.slider("Nr", min_value=1, max_value=100, value=10, step=1)
# Ne = st.sidebar.slider("Ne", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
MAX = st.sidebar.slider("MAX", min_value=1, max_value=100, value=50, step=1)
initial_p = st.sidebar.slider("Prior probability of this action being relevant", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
n_successes = st.sidebar.slider("n_successes experienced by recommending this action", min_value=1, max_value=100, value=10, step=1)
n_failures = st.sidebar.slider("n_failures experienced by recommending this action", min_value=1, max_value=100, value=10, step=1)

# Initialize parameters
alpha0 = initial_p * Nr + 1  # prior alpha
beta0 = (1 - initial_p) * Nr + 1  # prior beta

# Make sure the posterior contribution caps at MAX
if n_successes + n_failures > MAX:
    scaling_factor = MAX / (n_successes + n_failures)
    n_successes = n_successes * scaling_factor
    n_failures = n_failures * scaling_factor

alpha_posterior = min(n_successes + alpha0, MAX)
beta_posterior = min(n_failures + beta0, MAX)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 1, 1000)
y = np.random.beta(alpha_posterior, beta_posterior, 10000)  # Generate beta-distributed random numbers

ax.hist(y, bins=50, density=True, alpha=0.7, color='blue')
ax.set_title(f'Beta Distribution (α={alpha_posterior:.2f}, β={beta_posterior:.2f})')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 1)

# Display the plot in Streamlit
st.pyplot(fig)

# Display current parameter values
st.sidebar.markdown("### Current Values")
st.sidebar.write(f"Alpha (posterior): {alpha_posterior:.2f}")
st.sidebar.write(f"Beta (posterior): {beta_posterior:.2f}")