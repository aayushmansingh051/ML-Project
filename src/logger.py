# The sys module in Python provides various functions and variables that are used 
# to manipulate different parts of the Python runtime environment. 
# It allows us to fetch exception details like type, value, and traceback.
import sys

# Now logger is for the purpose that any execution that probably happens, 
# we should be able to log all that information (execution steps, errors, etc.) 
# into some files so that we can track issues later.
# If there are errors, even custom exceptions, we will log them into a text file.
import logging   # used to write logs into a file
import os        # used to create directories for logs
from datetime import datetime   # used to generate timestamped log file names

# -------------------------------
# Custom Exception Handling
# -------------------------------
def error_message_detail(error, error_detail: sys):
    # exc_info() returns (type, value, traceback). We only need the traceback object.
    _, _, exc_tb = error_detail.exc_info()
    
    # From traceback, we can extract the filename where the error occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format a detailed error message with filename, line number, and error text.
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    # Override the init method to customize exception behavior
    def __init__(self, error_message, error_detail: sys):
        # Call the base Exception class constructor
        super().__init__(error_message)
        # Generate a detailed error message using our helper function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # When we raise the custom exception, printing it will show the detailed message
    def __str__(self):
        return self.error_message


# -------------------------------
# Logging Configuration
# -------------------------------
# Every time you run the program, it generates a unique log file name 
# based on the exact timestamp. This prevents overwriting old logs.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a "logs" folder inside the current working directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)   # ensures folder exists

# Full path to the log file inside the logs folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging: write logs into the file with detailed format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s [%(lineno)d] %(name)s %(levelname)s %(message)s",
    level=logging.INFO,
)


# -------------------------------
# Main Execution Block
# -------------------------------
if __name__ == "__main__":
    try:
        a = 1 / 0   # this will cause ZeroDivisionError
    except Exception as e:
        # Log that logging has started
        logging.info("Logging has started")
        # Log the specific error message
        logging.error("Divide by Zero error occurred")
        # Raise our custom exception with detailed info
        # Note: Python will show both the original error (ZeroDivisionError) 
        # and our CustomException, because we raised a new exception while handling the first one.
        raise CustomException(e, sys)





#LOGGING:->
#Logging in programming (and computing in general) means recording events, actions, or messages
#  that happen while a program or system is running. Think of it like a diary or journal your program keeps, so you can later review what happened.
#🔑 Why Logging is Important
#Debugging → Helps you trace errors and see what went wrong.

#Monitoring → Lets you check if your program is working as expected.

#Auditing → Provides a history of actions (important for compliance and security).

#Performance tracking → Shows how long tasks take or where bottlenecks occur.