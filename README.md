https://complex-dpuynusovshtv9o9yaz5j9.streamlit.app/
# 🔥 Wildfire Prediction System using NetLogo and Machine Learning

## Project Overview

This project combines **Agent-Based Modeling (NetLogo)** and **Machine Learning** to predict wildfire simulation outcomes.

The NetLogo Fire model was used to simulate wildfire spread under different environmental conditions. The simulation results were exported as a CSV dataset and used to train a **Random Forest Regression** model. The trained model was then integrated into a **Streamlit** web application for real-time predictions.

---

## Problem Statement

Running NetLogo simulations repeatedly for different wildfire conditions can be time-consuming.

This project aims to predict wildfire simulation outcomes instantly using a trained machine learning model instead of rerunning the simulation.

---

## Objectives

- Simulate wildfire spread using NetLogo.
- Generate a dataset from the simulation.
- Train a Machine Learning model.
- Evaluate model performance.
- Deploy a prediction system using Streamlit.

---

## Technologies Used

- NetLogo 7.0
- Python
- Pandas
- Scikit-learn
- Random Forest Regressor
- Joblib
- Streamlit

---

## Dataset

The dataset was generated using the NetLogo Fire simulation.

Input Features:
- Forest Density
- Wind
- Simulation Step

Target Variable:
- Count Turtles

---

## Machine Learning Workflow

1. Generate wildfire simulation data using NetLogo.
2. Export the simulation data as a CSV file.
3. Load the dataset using Pandas.
4. Split the dataset into training and testing sets.
5. Train a Random Forest Regression model.
6. Evaluate the model using R² Score and MAE.
7. Save the trained model.
8. Build a Streamlit application for prediction.

---

## Project Structure

```
WildFire/
│
├── app.py
├── train.py
├── Fire experiment-table.csv
├── model.pkl
├── requirements.txt
└── README.md
```

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train.py
```

### Run the Streamlit application

```bash
python -m streamlit run app.py
```

---

## Model Performance

Model Used:
- Random Forest Regressor

Evaluation Metrics:
- R² Score
- Mean Absolute Error (MAE)

---

## Streamlit Application

The application allows users to enter:

- Forest Density
- Wind Speed
- Simulation Step

The trained model predicts the expected **Count Turtles** instantly.

---

## Future Improvements

- Include additional wildfire factors such as humidity and temperature.
- Compare multiple machine learning algorithms.
- Deploy the application on Streamlit Community Cloud.
- Improve prediction accuracy using larger datasets.

---

## Authors

Group Assignment

Department of Information Systems

Faculty of Computing

University of Sri Jayewardenepura

Sri Lanka
