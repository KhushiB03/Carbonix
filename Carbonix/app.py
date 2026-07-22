import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Carbonix", page_icon="🌱")

st.title("🌱 Carbonix")
st.write("Business Travel Carbon Predictor")

# Load model
model = joblib.load("Carbonix/xgboost_model.pkl")
columns = joblib.load("Carbonix/columns.pkl")

# ==========================
# Inputs
# ==========================

departure_country = st.selectbox(
    "Departure Country",
    ["AU","BR","CN","DE","JP","US","ZA"]
)

departure_city = st.text_input("Departure City")

arrival_country = st.selectbox(
    "Arrival Country",
    ["CN","DE","ES","FR","GB","IN","MX","SG","TR","ZA"]
)

arrival_city = st.text_input("Arrival City")

shipping = st.selectbox(
    "Travel Mode",
    [
        "Economy Flight",
        "Business Class Flight",
        "First Class Flight",
        "Train",
        "BMW 3 diesel",
        "Volkswagen Golf petrol"
    ]
)

purpose = st.selectbox(
    "Purpose",
    [
        "Customer Visit",
        "Conference/Exhibition",
        "Internal Business Trip",
        "Enablement"
    ]
)

out_policy = st.selectbox(
    "Out Of Policy",
    ["No", "Yes"]
)

business_unit = st.selectbox(
    "Business Unit",
    [
        "Services",
        "Sales",
        "Marketing",
        "Finance",
        "Customer Support",
        "Executive Management",
        "Ecosystem"
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

# ==========================
# Prediction
# ==========================

if st.button("Predict"):

    input_data = pd.DataFrame({
        "DepartureLocationCountry":[departure_country],
        "DepartureLocationCity":[departure_city],
        "ArrivalLocationCountry":[arrival_country],
        "ArrivalLocationCity":[arrival_city],
        "ShippingTypeDescription":[shipping],
        "Purpose":[purpose],
        "OutOfPolicy":[out_policy],
        "BusinessUnit":[business_unit],
        "HotelNights":[hotel_nights],
        "NetCosts":[net_cost]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    score = int(probability[1] * 100)

    st.subheader("🌱 Carbon Impact")

    st.progress(score)

    st.metric("Carbon Score", f"{score}%")

    if prediction == 1:
        st.error("🔴 High Carbon Trip")
    else:
        st.success("🟢 Low Carbon Trip")

    st.write("Confidence")

    st.write(f"Low Carbon : {probability[0]*100:.2f}%")
    st.write(f"High Carbon : {probability[1]*100:.2f}%")