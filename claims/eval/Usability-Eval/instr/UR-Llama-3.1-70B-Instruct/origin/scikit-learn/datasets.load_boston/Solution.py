# Importing necessary libraries
from sklearn import datasets
import pandas as pd
import numpy as np

# Load and return the boston house-prices dataset (regression)
def load_boston_dataset():
    """
    Load and return the boston house-prices dataset (regression)
    
    Returns:
        sklearn.utils.Bunch
    """
    # Load the boston dataset
    boston = datasets.fetch_california_housing()  # Replaced load_boston with fetch_california_housing
    
    # Convert the dataset into DataFrame
    boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
    boston_df['target'] = boston.target
    
    # Return the dataset
    return boston

# Example usage
boston_dataset = load_boston_dataset()
print(boston_dataset.data)
print(boston_dataset.target)
print(boston_dataset.feature_names)
