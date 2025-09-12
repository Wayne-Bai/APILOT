import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml

# Load the Boston Housing dataset from OpenML
boston = fetch_openml(name='boston', version=1, as_frame=True)

# Convert the dataset to a pandas DataFrame
boston_df = boston.frame

# Separate the features and target variable
X = boston_df.drop('MEDV', axis=1)
y = boston_df['MEDV']

# Print the first few rows of the dataset
print(boston_df.head())
