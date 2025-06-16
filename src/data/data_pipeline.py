import yfinance as yf
import pandas as pd
from datetime import datetime
from database.db_connection import connect_to_cloud_sql


def fetch_and_store_data(symbols):
    try:
        data = yf.download(symbols, period ='1d',interval='5m')

        processed_data =[]
        for symbol in symbols:
            symbol_data = data['Close'][symbol].dropna()
            for timestamp, price in symbol_data.items():
                processed_data.append({
                    'symbol':symbol,
                    'timestamp':timestamp,
                    'close_price':price
                })

        
        df = pd.DataFrame(processed_data)
        engine = connect_to_cloud_sql()
        df.to_sql('stock_prices',engine,if_exists='append', index= False)

        print(f"Successfully stored {len(df)} records ")

    except Exception as e:
        print(f"Error in data pipeline:{e}")


symbols =['AAPL','MSFT','GOOGL']
fetch_and_store_data(symbols)
