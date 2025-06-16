import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

def fetch_alpha_vantage_data(symbol):
    url = "https://www.alphavantage.co/query"
    params = {
        "function":"TIME_SERIES_INTRADAY",
        "symbol":symbol,
        "interval":"1min",
        "apikey":api_key,
        "datatype":"json"
    }

    response = requests.get(url, params =params)
    data = response.json()

    if "Time Series (1min)" in data:
        df =pd.DataFrame.from_dict(data["Time Series (1min)"], orient='index')
        df = df.rename(columns = lambda x :x[3:])
        df.index = pd.to_datetime(df.index)
        return df.sort_index()

    else:
        print(f"Error:{data}")
        return None
    
df = fetch_alpha_vantage_data("AAPL")
if df is not None:
    print(df.head())