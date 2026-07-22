if st.button("Predict Carbon Category"):

    input_data = pd.DataFrame({
        "distance": [distance],
        "arrival_city": [arrival_city],
        "mode": [mode]
    })

    # One-hot encode categorical variables
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Predict class
    prediction = model.predict(input_data)[0]

    # Predict probability (optional)
    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🔴 High Carbon Emission Trip")
        st.write(f"Confidence: **{probability[1] * 100:.2f}%**")
    else:
        st.success("🟢 Low Carbon Emission Trip")
        st.write(f"Confidence: **{probability[0] * 100:.2f}%**")