# Import necessary libraries
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class DataTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Define your data transformation here
        # For example, we will apply normalization to numerical columns and
        # one-hot encoding to categorical columns
        numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
        categorical_cols = X.select_dtypes(include=['object']).columns

        X[numerical_cols] = (X[numerical_cols] - X[numerical_cols].mean()) / X[numerical_cols].std()

        one_hot = pd.get_dummies(X[categorical_cols])
        X = pd.concat([X[numerical_cols], one_hot], axis=1)

        return X

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': ['apple', 'banana', 'orange', 'grape']
}
df = pd.DataFrame(data)

# Create an instance of the DataTransformer class
transformer = DataTransformer()

# Fit and transform the data
transformed_data = transformer.fit_transform(df)

print(transformed_data)
