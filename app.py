import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Customer Churn Prediction System")
st.write("Enter customer details to predict churn")

# --- Collect inputs for all 30 features ---
# Example: I'll show 10 numeric/categorical inputs; fill all 30 based on your dataset
tenure = st.number_input("Tenure", 0, 100)
monthly_charges = st.number_input("Monthly Charges", 0.0, 1000.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

# Example categorical inputs (convert to numeric if needed)
gender = st.selectbox("Gender", ["Male", "Female"])
gender_val = 1 if gender == "Male" else 0

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
contract_val = [0, 0, 0]  # One-hot encoding
if contract == "Month-to-month":
    contract_val = [1, 0, 0]
elif contract == "One year":
    contract_val = [0, 1, 0]
else:
    contract_val = [0, 0, 1]

# --- Add the remaining features here ---
# For simplicity, you can use default 0 values for unused features
other_features = [0] * 23  # Adjust length to match total 30 features

# --- Combine all features in correct order ---
input_features = [tenure, monthly_charges, total_charges, gender_val] + contract_val + other_features
input_array = np.array(input_features).reshape(1, -1)  # Shape (1,30)

# --- Predict ---
if st.button("Predict"):
    prediction = model.predict(input_array)
    st.write("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")

