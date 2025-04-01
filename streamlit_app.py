import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file not found. Please check the file path and try again.")
    st.stop()

# App Title
st.title("Salary Prediction App")
st.markdown("This application predicts salary based on years of experience.")

# User Input
experience = st.number_input('Enter Your Years of Experience:', min_value=0, max_value=50, step=1)
user_input = np.array([[experience]])

# Prediction
if st.button('Predict Salary'):
    prediction = model.predict(user_input).round(2)
    st.success(f"Predicted Salary: ₹{prediction[0]:,.2f}")
