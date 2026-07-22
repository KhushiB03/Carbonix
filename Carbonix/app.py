# =========================
# Prediction
# =========================

if st.button("🌱 Predict Carbon Impact"):

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

    # One-hot encoding
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    # Probability of High Carbon class
    carbon_score = int(probabilities[1] * 100)

    st.markdown("## 🌱 Carbon Impact Meter")

    st.progress(carbon_score)

    st.metric(
        label="Carbon Impact Score",
        value=f"{carbon_score}/100"
    )

    if carbon_score <= 25:
        st.success("🟢 Very Low Carbon Impact")
        st.write("This trip is expected to have a relatively low environmental impact.")

    elif carbon_score <= 50:
        st.info("🟡 Low Carbon Impact")
        st.write("This trip has a low carbon footprint compared to similar business trips.")

    elif carbon_score <= 75:
        st.warning("🟠 Moderate Carbon Impact")
        st.write("Consider greener travel options such as trains, direct flights, or reducing hotel nights.")

    else:
        st.error("🔴 High Carbon Impact")
        st.write("This trip is predicted to generate a high carbon footprint. Consider alternative travel options.")

    with st.expander("View Model Confidence"):
        st.write(f"Low Carbon Probability : **{probabilities[0]*100:.2f}%**")
        st.write(f"High Carbon Probability : **{probabilities[1]*100:.2f}%**")