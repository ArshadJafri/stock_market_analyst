
import os
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def connect_to_cloud_sql():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_USERNAME')
    database = os.getenv('DB_NAME')

    connection_string = f"postgresql://{user}:{password}@{host}:5432/{database}"
    engine = create_engine(connection_string)
    return engine

def test_connection():
    try:
        engine = connect_to_cloud_sql()
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("Database Connected Successfully")
        return True
    
    except Exception as e:
        print(f"Connection Failed :{e}")
        return False
    