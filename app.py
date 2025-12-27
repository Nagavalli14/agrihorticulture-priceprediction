import streamlit as st

st.title("Agri Commodity Price Prediction System")
st.write("Decision Support Tool for Buffer Stock Management")

# Define average price (based on training data)
average_price = 3000  # example value (₹/quintal)

price = st.number_input(
    "Enter Predicted Modal Price (₹/quintal)",
    min_value=0
)

if st.button("Get Buffer Stock Decision"):
    if price > average_price * 1.2:
        st.success("✅ Release Buffer Stock")
    else:
        st.info("ℹ️ Hold Buffer Stock")
