import streamlit as st
import pandas as pd
import joblib

st.title("Agri Commodity Price Prediction")

st.write("Predict prices & buffer stock decisions")

price = st.number_input("Enter Expected Modal Price")

if st.button("Get Decision"):
    if price > average_price * 1.2:
        st.success("Release Buffer Stock")
    else:
        st.info("Hold Buffer Stock")
