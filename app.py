from src.ML.logger import logging  # type: ignore
from src.ML.exception import CustomException
import sys
from src.ML.components.data_ingestion import  DataIngestion
from src.ML.components.data_ingestion import  DataIngestionConfig
if __name__ == "__main__":
    logging.info("the exceutation has started")
    

    try:
       #data_ingestion = DataIngestionConfig()
       data_ingestion = DataIngestion()
       data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info('custom exception')
        raise CustomException(e,sys)

    