import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

st.title("🔥 Wildfire Prediction System")

st.write("Enter the simulation values below:")

density = st.number_input("Tree Density", min_value=0, value=30)
wind = st.number_input("Wind Speed", min_value=0, value=0)
step = st.number_input("Simulation Step", min_value=0, value=0)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "density": [density],
        "wind": [wind],
        "[step]": [step]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Count of Turtles: {prediction[0]:.2f}")