import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Import custom exception and logger from your project
from src.exception import CustomException
from src.logger import logging

# Import transformation classes
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


# -------------------------------
# Configuration class for file paths
# -------------------------------
@dataclass
class DataIngestionConfig:
    # Path where training dataset will be saved
    train_data_path: str = os.path.join("artifacts", "train.csv")
    # Path where testing dataset will be saved
    test_data_path: str = os.path.join("artifacts", "test.csv")
    # Path where raw dataset will be saved
    raw_data_path: str = os.path.join("artifacts", "data.csv")


# -------------------------------
# Data Ingestion class
# -------------------------------
class DataIngestion:
    def __init__(self):
        # Initialize configuration object
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Steps:
        1. Read the raw dataset
        2. Save the raw dataset into artifacts folder
        3. Split the dataset into train and test sets
        4. Save train and test sets into artifacts folder
        """
        logging.info("Entered the data ingestion method/component")
        try:
            # Step 1: Read raw dataset from notebook/data/stud.csv
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as DataFrame")

            # Step 2: Create artifacts folder if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Save raw dataset into artifacts/data.csv
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Step 4: Perform train-test split (80% train, 20% test)
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Save train and test datasets into artifacts folder
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Return file paths for train and test datasets
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # If any error occurs, raise a custom exception
            raise CustomException(e, sys)


# -------------------------------
# Run ingestion if executed directly
# -------------------------------
if __name__ == "__main__":
    # Create DataIngestion object
    obj = DataIngestion()

    # Run ingestion process
    train_data, test_data = obj.initiate_data_ingestion()

    # Initialize DataTransformation and run preprocessing
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
