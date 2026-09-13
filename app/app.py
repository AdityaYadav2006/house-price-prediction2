import os
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Get the folder where this script is located, so paths work no matter where streamlit is run from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load saved model and columns
model = joblib.load(os.path.join(BASE_DIR, '../models/house_price_model.pkl'))
columns = joblib.load(os.path.join(BASE_DIR, '../models/model_columns.pkl'))

st.title("🏠 Bengaluru House Price Predictor")
st.write("Enter house details to get an estimated price (in Lakhs)")

# User inputs
sqft = st.number_input("Total Sqft", min_value=200, max_value=10000, value=1000)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
balcony = st.number_input("Balconies", min_value=0, max_value=5, value=1)
bhk = st.number_input("BHK", min_value=1, max_value=10, value=2)

location_columns = [col for col in columns if col not in ['total_sqft', 'bath', 'balcony', 'bhk']]
location = st.selectbox("Location", sorted(location_columns))

if st.button("Predict Price"):
    x = np.zeros(len(columns))
    x[columns.index('total_sqft')] = sqft
    x[columns.index('bath')] = bath
    x[columns.index('balcony')] = balcony
    x[columns.index('bhk')] = bhk
    if location in columns:
        x[columns.index(location)] = 1

    prediction = model.predict([x])[0]
    st.success(f"Estimated Price: ₹ {prediction:.2f} Lakhs")