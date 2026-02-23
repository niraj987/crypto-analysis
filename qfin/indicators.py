import pandas as pd
import numpy as np

def calculate_sma(data, window, column='Close'):
    """
    Calculates the Simple Moving Average (SMA).
    """
    return data[column].rolling(window=window).mean()

def calculate_ema(data, window, column='Close'):
    """
    Calculates the Exponential Moving Average (EMA).
    """
    return data[column].ewm(span=window, adjust=False).mean()

def calculate_rsi(data, window=14, column='Close'):
    """
    Calculates the Relative Strength Index (RSI).
    """
    # Calculate price changes
    delta = data[column].diff()
    
    # Separate gains and losses
    gain = delta.clip(lower=0)
    loss = -1 * delta.clip(upper=0)
    
    # Calculate average gain and average loss
    avg_gain = gain.rolling(window=window, min_periods=window).mean()
    avg_loss = loss.rolling(window=window, min_periods=window).mean()
    
    # Calculate RS
    rs = avg_gain / avg_loss
    
    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))
    return rsi
