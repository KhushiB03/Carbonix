import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Carbonix", page_icon="🌱")

st.title("🌱 Carbonix")
st.write("Business Travel Carbon Prediction")


# Load model and columns
model = joblib.load("xgboost_model.pkl")
columns = joblib.load("columns.pkl")

st.success("Model loaded successfully!")


st.subheader("Enter Travel Details")

# Example inputs (change names according to your dataset)
distance = st.number_input("Travel Distance (km)")
employees = st.number_input("Number of Employees")
mode = st.selectbox(
    "Travel Mode",
    ["Flight", "Train", "Car"]
)


if st.button("Predict Carbon Emission"):

    input_data = pd.DataFrame({
        "distance": [distance],
        "employees": [employees],
        "mode": [mode]
    })


    # One hot encoding
    input_data = pd.get_dummies(input_data)


    # Match training columns
    input_data = input_data.reindex(
        columns=columns,
        fill_value=0
    )


    prediction = model.predict(input_data)


    st.success(
        f"Predicted Carbon Emission: {prediction[0]}"
    )