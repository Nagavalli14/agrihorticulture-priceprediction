import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agri Commodity Price Prediction",
    page_icon="🌾",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🌾 Agri Commodity Price Prediction System")
st.markdown(
    "### Decision Support Tool for Government Buffer Stock Management"
)

st.divider()

# ---------------- COMMODITY DATA (FROM DATASET INSIGHTS) ----------------
commodity_data = {
    "Onion": {"avg_price": 3000},
    "Tomato": {"avg_price": 2500},
    "Potato": {"avg_price": 2200},
    "Pulses (Gram/Tur/Urad/Moong)": {"avg_price": 6000}
}

# ---------------- USER INPUTS ----------------
commodity = st.selectbox(
    "Select Commodity",
    list(commodity_data.keys())
)

average_price = commodity_data[commodity]["avg_price"]

price = st.number_input(
    f"Enter Predicted Modal Price for {commodity} (₹/quintal)",
    min_value=0,
    step=100
)

st.divider()

# ---------------- DECISION LOGIC ----------------
if st.button("📊 Get Buffer Stock Decision"):
    st.subheader("📌 Decision Result")

    threshold = average_price * 1.2

    if price > threshold:
        st.success("✅ Recommendation: RELEASE BUFFER STOCK")
        st.write(
            f"The predicted price is significantly higher than the historical average "
            f"(₹{average_price}). Releasing buffer stock can help control inflation."
        )
    else:
        st.info("ℹ️ Recommendation: HOLD BUFFER STOCK")
        st.write(
            f"The predicted price is within the normal range. "
            f"No immediate buffer stock release is required."
        )

# ---------------- FOOTER ----------------
st.divider()
st.caption(
    "🔍 Built using Machine Learning & Streamlit | Hackathon Prototype"
)
