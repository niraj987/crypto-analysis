import yfinance as yf
import pandas as pd

def fetch_crypto_data(ticker, period='1y', interval='1d'):
    """
    Fetches historical historical cryptocurrency data using yfinance.
    
    Args:
        ticker (str): The Yahoo Finance ticker for the cryptocurrency (e.g., 'BTC-USD', 'ETH-USD').
        period (str): The time period to fetch data for (e.g., '1mo', '3mo', '1y', 'max').
        interval (str): The interval of the data (e.g., '1d', '1wk', '1mo').
        
    Returns:
        pandas.DataFrame: Historical price data (Open, High, Low, Close, Volume).
    """
    try:
        print(f"Fetching data for {ticker}...")
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            print(f"Warning: No data found for {ticker}.")
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()
