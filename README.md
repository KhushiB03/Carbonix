# 🌱 Carbonix – Business Travel Carbon Emission Predictor

## Overview

Carbonix is a machine learning-powered web application built with **Streamlit** that helps organizations estimate the environmental impact of business travel. The application analyzes travel-related information and classifies a trip as either **High Carbon** or **Low Carbon** based on historical travel data.

The project demonstrates the use of machine learning for sustainability by enabling businesses to understand the carbon impact of employee travel and encourage greener travel decisions.

---

## Features

* 🌍 Predicts whether a business trip is **High Carbon** or **Low Carbon**
* ✈️ Supports multiple travel modes such as flights, trains, and vehicles
* 🏙️ Considers departure and arrival locations
* 🏨 Includes hotel stay information
* 💰 Uses trip cost and travel details for prediction
* 📊 Interactive web interface built using Streamlit
* ⚡ Fast predictions using an XGBoost machine learning model

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* XGBoost
* Joblib

---

## Dataset

The dataset contains historical business travel records with attributes such as:

* Trip ID
* Departure Country
* Departure City
* Arrival Country
* Arrival City
* Shipping Type
* Shipping Type Description
* Travel Purpose
* Out of Policy Status
* Business Unit
* Hotel Nights
* Net Costs
* Carbon Emissions

  * Departure CO₂e
  * Return CO₂e
  * Hotel CO₂e
  * Spend CO₂e
  * Total CO₂e
* HighCarbon (Target Variable)

---

## Machine Learning Model

The application uses an **XGBoost Classifier** trained on historical travel data.

### Target

* **0** → Low Carbon Trip
* **1** → High Carbon Trip

### Workflow

1. Load the travel dataset.
2. Perform preprocessing and one-hot encoding.
3. Train the XGBoost classifier.
4. Save the trained model using Joblib.
5. Load the model in the Streamlit application.
6. Predict whether a trip belongs to the High Carbon or Low Carbon category.

---

## Project Structure

```text
Carbonix/
│
├── app.py
├── xgboost_model.pkl
├── columns.pkl
├── requirements.txt
├── travel_data.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/KhushiB03/Carbonix.git
cd carbonix
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Input Parameters

Users can provide:

* Departure Country
* Departure City
* Arrival Country
* Arrival City
* Travel Mode
* Travel Purpose
* Business Unit
* Hotel Nights
* Net Cost
* Out of Policy Status

---

## Output

The application predicts:

* 🟢 Low Carbon Trip
* 🔴 High Carbon Trip

along with the prediction confidence.

---

## Future Improvements

* Carbon emission regression model for exact CO₂ prediction
* Interactive dashboards and analytics
* Carbon reduction recommendations
* Flight distance calculation using maps
* Support for real-time travel APIs
* Visualization of carbon trends

---

## Author

Developed as a Machine Learning and Streamlit project to promote sustainable business travel through carbon emission analysis.
