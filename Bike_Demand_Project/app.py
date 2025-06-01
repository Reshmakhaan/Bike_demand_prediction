import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load model (you’ll train and save this)
model = pickle.load(open("bike_model.pkl", "rb"))

st.title("🚴 Bike Demand Predictor")
st.write("Enter environmental and time conditions to predict bike rental count:")

# User inputs
season = st.selectbox("Season (1=spring, 2=summer, 3=fall, 4=winter)", [1, 2, 3, 4])
hr = st.slider("Hour of the Day", 0, 23, 12)
holiday = st.selectbox("Holiday (0=No, 1=Yes)", [0, 1])
weekday = st.slider("Weekday (0=Sunday ... 6=Saturday)", 0, 6, 3)
workingday = st.selectbox("Working Day (0=No, 1=Yes)", [0, 1])
weathersit = st.selectbox("Weather Situation (1=Clear, 2=Mist, 3=Light Rain/Snow)", [1, 2, 3])
temp = st.slider("Temperature (Normalized 0 to 1)", 0.0, 1.0, 0.5)
hum = st.slider("Humidity (Normalized 0 to 1)", 0.0, 1.0, 0.5)
windspeed = st.slider("Windspeed (Normalized 0 to 1)", 0.0, 1.0, 0.2)

# Predict
features = [[season, 1, 1, hr, holiday, weekday, workingday, weathersit, temp, hum, windspeed]]
prediction = model.predict(features)

st.success(f"🎯 Predicted Bike Count: {int(prediction[0])}")
