""" import streamlit as st
import pickle
import numpy as np

st.title("Laptop Price Predictor")

st.write("A simple machine learning site to predict estimated laptop prices")

# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Create user input fields
Storage_Capacity = st.number_input("Enter Storage Capacity",
                          min_value=100, max_value=4000, value=500)
RAM_Size = st.number_input("Enter RAM size", 
                      min_value=2, max_value=128, value=8)
Weight = st.number_input("Enter Laptop Weight",
                         min_value=1, max_value=5, value=2)
Screen_Size = st.number_input("Enter Screen size",
                         min_value=10, max_value=15, value=11)
Processor_Speed = st.number_input("Enter Processor speed", 
                            min_value=1, max_value=10, value=2)


# Button for prediction
if st.button("Predict"):
    # Prepare the input array
    user_data = np.array([[Storage_Capacity, RAM_Size, Weight, Screen_Size,
                           Processor_Speed]])  # Add more inputs as necessary

    # Make prediction
    prediction = model.predict(user_data)

    # Show prediction result
    st.write(f"Prediction price: {prediction[0]:.2f}") """

import streamlit as st
import numpy as np
import pickle
import os

# Set page config with a title and a background color
st.set_page_config(page_title="Laptop Price Predictor 💻", layout="centered")

# Apply background color using HTML & CSS
page_bg = """
<style>
body {
    background-color: #f0f4f8;
}
.main {
    background-color: skyblue;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App Title with Emoji
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)

st.markdown("### Fill in the laptop specifications below:")
# Load the saved model
curr_path = "machine-learning/Laptop Price Prediction/"
model_path = os.path.join(curr_path, "model.pkl")

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# UI form for laptop features
with st.form("laptop_form"):
    col1, col2 = st.columns(2)

    with col1:
        brand = st.selectbox("Brand", ["Dell", "HP", "Lenovo", "Apple", "Asus", "Acer", "MSI"])
        Processor_Speed = st.slider("Processor speed", 1.0, 5.0, 2.0)
        RAM_Size = st.selectbox("RAM (GB)", [4, 8, 16, 32, 128])
        # ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024])
    
    with col2:
        Storage_Capacity = st.selectbox("Storage Capacity", [100, 500, 1000, 2000, 3000, 4000])
        Screen_Size = st.selectbox("Screen size", [10, 11, 12, 13, 14])
        os = st.selectbox("Operating System", ["Windows 10", "Windows 11", "macOS", "Linux"])
        Weight = st.slider("Weight (kg)", 1.0, 3.5, 1.5)

    submitted = st.form_submit_button("Predict Price 💰")
    user_data = np.array([[Storage_Capacity, RAM_Size, Weight, Screen_Size,
                           Processor_Speed]])
    prediction = model.predict(user_data)

    # Show prediction result
    

if submitted:
    with st.spinner("Predicting price..."):
        # simulate processing
        import time
        time.sleep(2)
        pred = prediction[0]

    st.success(f"💰 Predicted Price: ${pred:.2f}")
