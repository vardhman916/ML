import sys 
from src.ML.logger import logging




def error_message_detail(error_message,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    '''exc_type: The exception type (ignored here using _).
exc_value: The exception instance (ignored using _).
exc_tb: The traceback object (used here).'''
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
       file_name,exc_tb.tb_lineno,str(error_message) 
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message_detail(error_message,error_details)
        super().__init__(str(error_message))

    def __str__(self):
        return self.error_message