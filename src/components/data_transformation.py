import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
# For handling missing values
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Exception handling
from src.exception import CustomException   # corrected: class name should be capitalized
from src.logger import logging
import os

from src.utlis import save_object   # ⚠️ check spelling: should be utils.py not utlis.py


# -------------------------------
# Configuration class
# -------------------------------
@dataclass
class DataTransformationConfig:
    # Concept: we want to reuse the same preprocessing steps later (e.g. during prediction).
    # So we save the fitted ColumnTransformer object into a pickle file.
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


# -------------------------------
# Data Transformation class
# -------------------------------
class DataTransformation:
    def __init__(self):
        # Holds the config (where to save the preprocessor object)
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        Concept: Build two separate pipelines —
        - Numerical pipeline: handle missing values + scale numbers
        - Categorical pipeline: handle missing values + encode categories
        Then combine them into one ColumnTransformer so both run together.
        """
        try:
            # Numerical features are continuous scores → need scaling
            numerical_columns = ["writing_score", "reading_score"]

            # Categorical features are discrete labels → need encoding
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            # Numerical pipeline: median imputation avoids distortion from outliers,
            # scaling ensures all features are on comparable ranges.
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])

            # Categorical pipeline: impute with most frequent keeps categories valid,
            # one-hot encoding converts text labels into numeric vectors,
            # scaling after encoding helps algorithms that are sensitive to magnitude.
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")),
                ("scaler", StandardScaler(with_mean=False))
            ])

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            # ColumnTransformer: conceptually this is a “master pipeline”
            # that applies num_pipeline to numerical columns and cat_pipeline to categorical ones.
            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    # Start data transformation
    def initiate_data_transformation(self, train_path, test_path):
        """
        Concept: Apply the preprocessing object to both train and test sets.
        - Fit on train (learn imputation values, scaling parameters, encoding categories)
        - Transform both train and test using the same fitted object
        - Concatenate transformed features with target column
        - Save the preprocessor for future inference
        """
        try:
            # Load raw train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            # Build preprocessing pipelines
            preprocessing_obj = self.get_data_transformer_object()

            # Target column is what we want to predict
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            # Separate input features (X) and target (y)
            input_feature_train_df = train_df.drop(target_column_name, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(target_column_name, axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing dataframes")

            # Fit on training data (learn imputation values, scaling params, categories)
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            # Transform test data using the same fitted object (important to avoid leakage)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # np.c_ stacks arrays column-wise → here we append the target column back
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")

            # Save the fitted preprocessor object for later use (e.g. during prediction)
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj   # corrected typo
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
