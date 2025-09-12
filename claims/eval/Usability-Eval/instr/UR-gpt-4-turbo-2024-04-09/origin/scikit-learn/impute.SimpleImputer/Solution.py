import numpy as np
from sklearn.impute import SimpleImputer

# Example data with missing values
data = np.array([
    [7, 2, np.nan],
    [4, np.nan, 6],
    [10, 5, 9],
    [np.nan, 4, 5]
])

# Create imputer object with mean strategy
imputer = SimpleImputer(strategy='mean')

# Fit imputer model and transform data
imputed_data = imputer.fit_transform(data)

print("Original Data:")
print(data)

print("\nImputed Data with Mean Strategy:")
print(imputed_data)
