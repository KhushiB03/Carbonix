import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Carbonix", page_icon="🌱")

st.title("🌱 Carbonix")
st.subheader("Business Travel Carbon Classification")

# Load model and training columns
model = joblib.load("Carbonix/xgboost_model.pkl")
columns = joblib.load("Carbonix/columns.pkl")

# =========================
# User Inputs
# =========================

departure_country = st.text_input("Departure Country", "CN")
departure_city = st.text_input("Departure City", "Beijing")

arrival_country = st.text_input("Arrival Country", "IN")
arrival_city = st.text_input("Arrival City", "New Delhi")

shipping = st.selectbox(
    "Travel Mode",
    [
        "Business Class Flight",
        "Economy Class Flight",
        "First Class Flight",
        "Train",
        "Car"
    ]
)

purpose = st.selectbox(
    "Purpose",
    [
        "Customer Visit",
        "Internal Meeting",
        "Conference",
        "Training",
        "Sales Meeting"
    ]
)

out_policy = st.selectbox(
    "Out Of Policy",
    [
        "No",
        "Yes"
    ]
)

business_unit = st.selectbox(
    "Business Unit",
    [
        "Services",
        "Sales",
        "Finance",
        "HR",
        "Operations"
    ]
)

hotel_nights = st.number_input(
    "Hotel Nights",
    min_value=0,
    value=1
)

net_cost = st.number_input(
    "Net Cost",
    min_value=0.0,
    value=1000.0
)

# =========================
# Prediction
# =========================

if st.button("Predict"):

    input_data = pd.DataFrame({
        "DepartureLocationCountry": [departure_country],
        "DepartureLocationCity": [departure_city],
        "ArrivalLocationCountry": [arrival_country],
        "ArrivalLocationCity": [arrival_city],
        "ShippingTypeDescription": [shipping],
        "Purpose": [purpose],
        "OutOfPolicy": [out_policy],
        "BusinessUnit": [business_unit],
        "HotelNights": [hotel_nights],
        "NetCosts": [net_cost]
    })

    # One-hot encode
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction")

    if prediction == 1:
        st.error(
            f"🔴 High Carbon Trip\n\nConfidence: {probability[1]*100:.2f}%"
        )
    else:
        st.success(
            f"🟢 Low Carbon Trip\n\nConfidence: {probability[0]*100:.2f}%"
        )