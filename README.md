# 📊 Student Performance Prediction

An **end-to-end Machine Learning web application** that predicts a student's mathematics score based on demographic, academic, and preparation-related factors.

The project covers the complete ML lifecycle — from **data ingestion and exploratory data analysis to preprocessing, model training, model selection, prediction, and web deployment**.

## 🚀 Live Demo

🌐 **Live Application:**
https://ml-project-1-d4ml.onrender.com/

## 📌 Project Overview

Student performance can be influenced by several factors such as:

* Gender
* Race/Ethnicity
* Parental level of education
* Lunch type
* Test preparation course
* Reading score
* Writing score

This project uses these features to predict a student's **Mathematics Score** using machine learning regression models.

The application provides a simple web interface where users can enter student information and instantly receive a predicted mathematics score.

---

## ✨ Features

* 📥 Data ingestion and train-test splitting
* 🔍 Exploratory Data Analysis (EDA)
* 🧹 Missing-value handling
* 🔢 Numerical feature scaling
* 🔤 Categorical feature encoding
* 🤖 Multiple machine learning models
* ⚙️ Hyperparameter tuning
* 🏆 Automatic selection of the best-performing model
* 💾 Model and preprocessing object persistence
* 🔮 Real-time predictions
* 🌐 Flask-based web application
* 📱 Responsive user interface
* ☁️ Cloud deployment

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Ingestion
     ↓
Train-Test Split
     ↓
Exploratory Data Analysis
     ↓
Data Preprocessing
     ├── Missing Value Imputation
     ├── Standard Scaling
     └── One-Hot Encoding
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
Best Model Selection
     ↓
Model Serialization
     ↓
Flask Prediction Pipeline
     ↓
Web Application
     ↓
Predicted Mathematics Score
```

---

## 🤖 Machine Learning Models

The project evaluates multiple regression algorithms:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**
4. **Gradient Boosting Regressor**
5. **XGBoost Regressor**
6. **CatBoost Regressor**
7. **AdaBoost Regressor**

The models are evaluated using **R² Score**, and the best-performing model is selected automatically.

---

## ⚙️ Data Preprocessing

The preprocessing pipeline consists of:

### Numerical Features

* `reading_score`
* `writing_score`

Processing:

```text
Missing Value Imputation
        ↓
StandardScaler
```

### Categorical Features

* `gender`
* `race_ethnicity`
* `parental_level_of_education`
* `lunch`
* `test_preparation_course`

Processing:

```text
Missing Value Imputation
        ↓
One-Hot Encoding
        ↓
Scaling
```

A fitted preprocessing object is saved as:

```text
artifacts/preprocessor.pkl
```

This same preprocessing pipeline is reused during prediction to ensure consistency between training and inference.

---

## 📂 Project Structure

```text
ML-Project/
│
├── artifacts/
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* XGBoost
* CatBoost

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Development

* Flask
* HTML
* CSS
* JavaScript

### Deployment

* Render

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aayushmansingh051/ML-Project.git
```

### 2. Navigate to the Project

```bash
cd ML-Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000/
```

---

## 🔮 How Prediction Works

The user enters:

```text
Gender
Race/Ethnicity
Parental Education
Lunch Type
Test Preparation Course
Reading Score
Writing Score
```

The Flask application converts the submitted information into a Pandas DataFrame.

The prediction pipeline then:

```text
User Input
    ↓
CustomData
    ↓
DataFrame
    ↓
Saved Preprocessor
    ↓
Transformed Features
    ↓
Saved ML Model
    ↓
Prediction
    ↓
Predicted Mathematics Score
```

---

## 📈 Model Evaluation

The project uses **R² Score** to evaluate regression models.

The model selection process compares multiple algorithms and selects the model with the highest evaluation score.

A minimum performance threshold is also applied before accepting a model for deployment.

---

## 🌐 Application Interface

The web application provides:

* Clean and responsive interface
* Student information form
* Score sliders and numerical inputs
* Instant prediction
* Visual score gauge
* Performance classification

### Prediction Categories

|    Score | Category      |
| -------: | ------------- |
|   85–100 | Excellent     |
|    70–84 | Good          |
|    50–69 | Average       |
| Below 50 | Needs Support |

> The predicted score is an ML-based estimate and should not be considered a guaranteed academic result.

---

## 📚 Dataset

The project uses a **Student Performance dataset** containing demographic information, parental education, lunch type, test preparation status, and student examination scores.

The target variable is:

```text
math_score
```

Input features include:

```text
gender
race_ethnicity
parental_level_of_education
lunch
test_preparation_course
reading_score
writing_score
```

---

## 🔐 Model Persistence

The trained model and preprocessing pipeline are serialized using Python object serialization.

```text
artifacts/
│
├── model.pkl
└── preprocessor.pkl
```

This allows the deployed application to make predictions without retraining the model every time a user submits the form.

---

## 🧩 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

* Exploratory Data Analysis
* Feature Engineering
* Data Preprocessing
* Train-Test Split
* Pipeline Architecture
* Regression
* Model Comparison
* Hyperparameter Tuning
* Model Evaluation
* Model Serialization
* Exception Handling
* Logging
* Flask API/Web Application
* Machine Learning Deployment
* Git/GitHub

---
## 👨‍💻 Author

**Aayushman Singh**

B.Tech — Computer Science & Engineering (AI & ML)

GitHub:
https://github.com/aayushmansingh051
Live Demo:https://ml-project-1-d4ml.onrender.com/

---

## ⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.

**Built with Python, Machine Learning, Flask, and ❤️**
