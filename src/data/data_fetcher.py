import yfinance as yf
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv


def fetch_stock_data(symbols):

    try:
        data = yf.download(symbols, period ='1d',interval ='1m')
        return data['Close'].fillna(method = 'ffill')
    except Exception as e:
        print(f"Error fetching data:{e}")
        return None

tech_stocks = ['AAPL','MSFT', 'GOOGL','AMZN','TSLA']
stock_data = fetch_stock_data(tech_stocks)
print(stock_data.head())