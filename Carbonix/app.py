import streamlit as st
import joblib

st.set_page_config(page_title="Carbonix", page_icon="🌱")

st.title("🌱 Carbonix")
st.write("Business Travel Carbon Prediction")

model = joblib.load("Carbonix/xgboost_model.pkl")

st.success("Model loaded successfully!")

st.info("The prediction ... interface will be added next.")