import streamlit as st
import pandas as pd

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("cleaned_agri_prices.csv")

# Normalize column names (safety)
df.columns = df.columns.str.lower()

# -----------------------------
# App UI
# -----------------------------
st.title("🌾 Agri Commodity Price Prediction System")
st.write("Decision Support Tool for Government Buffer Stock Management")

# Commodity selection
commodity_list = sorted(df['commodity'].unique())
commodity = st.selectbox("Select Commodity", commodity_list)

# Filter data for selected commodity
commodity_data = df[df['commodity'] == commodity]

# Calculate average modal price
average_price = commodity_data['modal_price'].mean()

# Price input
price = st.number_input(
    "Enter Predicted Modal Price (₹ / quintal)",
    min_value=0.0,
    step=10.0
)

# -----------------------------
# Decision Logic
# -----------------------------
if st.button("Get Buffer Stock Decision"):
    st.write(f"📊 Historical Average Price: ₹{round(average_price,2)}")

    if price > average_price * 1.2:
        st.success("✅ Release Buffer Stock (Price too high)")
    elif price < average_price * 0.8:
        st.warning("🟡 Procure & Store Buffer Stock (Price too low)")
    else:
        st.info("ℹ️ Hold Buffer Stock (Price Stable)")
