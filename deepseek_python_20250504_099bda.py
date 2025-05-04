import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def train_lstm(data, lookback=60):
    """Train LSTM model on closing prices"""
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data[['Nifty']])
    
    # Create sequences
    X, y = [], []
    for i in range(len(scaled)-lookback):
        X.append(scaled[i:i+lookback])
        y.append(scaled[i+lookback])
    
    # Build model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(lookback, 1)),
        LSTM(50),
        Dense(1)
    ])
    model.compile(loss='mse', optimizer='adam')
    model.fit(np.array(X), np.array(y), epochs=10, verbose=0)
    
    return model, scaler