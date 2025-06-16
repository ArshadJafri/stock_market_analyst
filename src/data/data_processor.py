import pandas as pd
import numpy as np 
from datetime import datetime

def clean_stock_data(raw_data):

    cleaned_data = raw_data.dropna(how ='all')
    cleaned_data = cleaned_data.fillna(method = 'ffill')
    cleaned_data['timestamp'] = datetime.now()

    return cleaned_data

def calculate_returns(data):
    returns = data.pct_change().dropna()
    return returns

def add_risk_metrics(data):
    data['volatility'] = data.rolling(window=20).std()
    data['moving_average'] = data.rolling(window =20).mean()

    return data 