import yfinance as yf
import pandas as pd

def fetch_data():
    """Fetch Nifty and VIX data"""
    nifty = yf.download("^NSEI", period="5y")['Close'].rename('Nifty')
    vix = yf.download("^INDIAVIX", period="5y")['Close'].rename('VIX')
    return pd.concat([nifty, vix], axis=1).dropna()