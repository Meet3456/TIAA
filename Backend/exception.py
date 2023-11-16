
import sys


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] , Line Number [{1}] and Error message is [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

## Custom Exception Class:Inherting Exception Class:
class CustomException(Exception):
    ## Constructor:
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error=error_message,error_detail=error_detail)
    ## For printing Error message:
    def __str__(self):
        return self.error_message

