import streamlit as st
import numpy as np
import joblib

# Load your trained model (ensure the path is correct)
model_path = "C:/Users/user/Desktop/Landslide prediction/ML_MODEL/random_forest_model.pkl"
model = joblib.load(model_path)

st.title("Landslide Prediction")

st.write("Enter the required parameters")

longitude = st.number_input("Longitude", min_value=-1, max_value=5, value=0.0)
latitude = st.number_input("Latitude", min_value=-1, max_value=5, value=0.0)
latitude = st.number_input("Latitude", min_value=-1, max_value=5, value=0.0)
latitude = st.number_input("Latitude", min_value=-1, max_value=5, value=0.0)
latitude = st.number_input("Latitude", min_value=-1, max_value=5, value=0.0)
latitude = st.number_input("Latitude", min_value=-1, max_value=5, value=0.0)

if st.button("Predict"):
    user_input = np.array([[longitude, latitude]])
    prediction = model.predict(user_input)
    st.write(prediction)