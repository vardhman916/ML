import os
import sys
from src.ML.exception import CustomException
from src.ML.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv() # Load environment variables from .env file

host = os.getenv("host")
user = os.getenv("user")
passs = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQl database started")
    try:
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = passs,
            db = db
        )
        logging.info("connection establish", mydb)
        df = pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        return df

    except Exception as ex:
       raise CustomException(ex,sys) 