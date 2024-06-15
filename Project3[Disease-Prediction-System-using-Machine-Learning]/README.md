#Disease Prediction System Using Machine Learning

## Project Overview

This project aims to predict the likelihood of heart disease based on various health-related attributes using machine learning algorithms. The workflow includes data preprocessing, feature selection, and training multiple models to determine the best predictive performance.

## Repository Contents

- `NEXUS.ipynb`: Jupyter notebook containing the complete workflow of data preprocessing, feature selection, model training, and evaluation.
- `heart_disease.csv`: The dataset used for the project (ensure this is in your working directory).

## Dataset

The dataset `heart_disease.csv` contains health-related information of individuals, including whether they have experienced heart disease or a heart attack. The dataset includes various attributes such as blood pressure, cholesterol levels, BMI, smoking status, physical activity, and other lifestyle and health indicators. These features are used to predict the target variable, which indicates the presence or absence of heart disease or a heart attack.

## Project Workflow

### 1. Data Loading and Exploration
- Load the dataset using `pandas`.
- Conduct initial exploration to understand the structure, data types, and basic statistics.

### 2. Data Preprocessing
- Handle missing values by removing rows with any missing data.
- Convert categorical variables into numeric formats if necessary.
- Normalize or standardize numerical features for better performance of machine learning algorithms.

### 3. Feature Selection
- Drop less relevant or redundant features to simplify the model.
- Optionally, use feature selection techniques such as `SelectKBest` with ANOVA F-test to choose the most significant features.

### 4. Model Training and Evaluation
- Split the data into training and testing sets using `train_test_split`.
- Train various machine learning models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
- Evaluate models using cross-validation and metrics such as accuracy, precision, recall, and F1 score.
- Select the best performing model based on evaluation metrics.

## How to Run the Project

### Prerequisites

- Python 3.x
- Jupyter Notebook

## Dependencies

The project requires the following Python libraries:
- pandas
- numpy
- scikit-learn
- Jupyter Notebook


## Project Details

### Data Preprocessing

- **Handling Missing Values**: Missing values are handled by removing rows with any missing entries.
- **Feature Transformation**: Features are selected based on relevance to the target variable, with some being dropped to reduce complexity.
- **Normalization**: Numerical features are scaled to a standard range to improve model performance.

### Feature Selection

- **Manual Selection**: Certain features deemed less relevant are manually dropped.
- **Automated Selection**: Techniques like `SelectKBest` are used to identify and retain the most significant features for the predictive model.

### Model Training

- **Logistic Regression**: Used for binary classification, providing probabilities for class membership.
- **Decision Tree**: A non-linear model that splits data based on feature values.
- **Random Forest**: An ensemble method using multiple decision trees to improve robustness and accuracy.
- **Support Vector Machine (SVM)**: A powerful classifier that finds the optimal hyperplane to separate classes.

### Model Evaluation

Models are evaluated using:
- **Accuracy**: The ratio of correctly predicted instances to the total instances.
- **Precision**: The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall**: The ratio of correctly predicted positive observations to all observations in the actual class.
- **F1 Score**: The weighted average of precision and recall, especially useful for imbalanced datasets.

## Conclusion

This project demonstrates a comprehensive approach to predicting heart disease using machine learning. By following the steps outlined in the Jupyter notebook, you can preprocess data, select relevant features, train multiple models, and evaluate their performance to identify the best predictor.
