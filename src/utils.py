#utils=>this is a common functionality throught the entire application
import os
import sys
import dill   # make sure you import dill, otherwise dill.dump will fail
from src.exception import CustomException
from sklearn.metrics import  r2_score

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


from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    report = {}
    for model_name, model in models.items():
        try:
            # Fit the model on training data
            model.fit(X_train, y_train)

            # Predict on test data
            y_pred = model.predict(X_test)

            # Evaluate with R² score
            score = r2_score(y_test, y_pred)

            # Save score in report
            report[model_name] = score

        except Exception as e:
            print(f"Error training {model_name}: {e}")
    return report
# so, this load object is responsible for loading the pickel file
def load_object(file_path):
    try:
     with open(file_path, "rb") as file_obj:
        return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)