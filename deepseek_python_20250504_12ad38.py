import streamlit as st
from modules.data_loader import fetch_data
from modules.model_trainer import train_lstm
from modules.options_pricer import calculate_premium
import pandas as pd

# UI Config
st.set_page_config(page_title="Nifty Option Predictor", page_icon="📈")

# Sidebar
st.sidebar.header("Parameters")
days_ahead = st.sidebar.slider("Forecast Days", 1, 30, 7)
strike = st.sidebar.number_input("Strike Price", value=18000)
expiry_days = st.sidebar.number_input("Expiry Days", value=7)

# Main Logic
if st.button("Predict"):
    # Fetch Data
    df = fetch_data()
    
    # Train Model
    model, scaler = train_lstm(df)
    predicted_price = model.predict(df)[0][0]
    
    # Calculate Premium
    premium = calculate_premium(
        spot=df['Close'].iloc[-1],
        strike=strike,
        days_to_expiry=expiry_days
    )
    
    # Display Results
    col1, col2 = st.columns(2)
    col1.metric("Predicted Price", f"₹{predicted_price:.2f}")
    col2.metric("Call Premium", f"₹{premium:.2f}")
    
    # Chart
    st.line_chart(df['Close'][-100:])