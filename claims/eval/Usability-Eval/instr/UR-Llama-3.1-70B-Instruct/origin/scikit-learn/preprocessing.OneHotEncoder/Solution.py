# Import necessary libraries from scikit-learn
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd

# Sample categorical data
data = {
    'Country': ['USA', 'USA', 'Canada', 'Canada', 'USA', 'Canada'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Fit and Transform data
encoded_data = encoder.fit_transform(df)

# Get feature names
feature_names = encoder.get_feature_names_out()

# Create a DataFrame with encoded data
encoded_df = pd.DataFrame(encoded_data, columns=feature_names)

# Print the original and encoded data
print("Original Data:")
print(df)
print("\nEncoded Data:")
print(encoded_df)
