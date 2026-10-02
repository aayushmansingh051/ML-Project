#The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the
import sys

#custome exception handling 
def error_message_detail(error, error_detail: sys):
    #from this info we will be able to get information 
    # like on which file the exception occured, on which line exception occured
    _, _, exc_tb = error_detail.exc_info()   # exc_info() gives (type, value, traceback)
    file_name = exc_tb.tb_frame.f_code.co_filename   # corrected: tb_frame not tb_frane
    
    # format the error message with file name, line number, and error text
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message


class CustomException(Exception):
    #override the init methid
    def __init__(self, error_message, error_detail: sys):
        #inherit the exception class
        super().__init__(error_message)   # corrected: super().__init__ not super.__init__
        
        #self makes sure that when you call a method, it knows which object’s data to use.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    #when we raise the custome exception,in short we print it, its going to print the error message itself
    def __str__(self):
        return self.error_message
