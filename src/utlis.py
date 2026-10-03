import os
import sys
import dill   # make sure you import dill, otherwise dill.dump will fail
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save any Python object (like a trained model or preprocessor) into a pickle file using dill.
    Args:
        file_path (str): Path where the object will be saved
        obj (object): Python object to save
    """
    try:
        # Get the directory path from the file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in write-binary mode and dump the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # If anything goes wrong, raise your custom exception
        raise CustomException(e, sys)
