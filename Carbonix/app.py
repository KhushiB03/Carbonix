import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Carbonix", page_icon="🌱")

st.title("🌱 Carbonix")
st.write("Business Travel Carbon Prediction")

# Load model and columns
model = joblib.load("Carbonix/xgboost_model.pkl")
columns = joblib.load("Carbonix/columns.pkl")

st.success("Model loaded successfully!")

st.subheader("Enter Travel Details")

# User Inputs
distance = st.number_input(
    "Travel Distance (km)",
    min_value=0.0,
    value=100.0
)

arrival_city = st.selectbox(
    "Arrival City",
    [
        "Delhi",
        "Mumbai",
        "Bengaluru",
        "Chennai",
        "Hyderabad",
        "Kolkata",
        "Pune",
        "Ahmedabad"
    ]
)

mode = st.selectbox(
    "Travel Mode",
    ["Flight", "Train", "Car"]
)

# Predict
if st.button("Predict Carbon Emission"):

    input_data = pd.DataFrame({
        "distance": [distance],
        "arrival_city": [arrival_city],
        "mode": [mode]
    })

    # One-hot encode categorical features
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)

    st.write("Input to Model:")
    st.dataframe(input_data)

    st.success(
        f"🌱 Predicted Carbon Emission: {prediction[0]:.2f} kg CO₂"
    )