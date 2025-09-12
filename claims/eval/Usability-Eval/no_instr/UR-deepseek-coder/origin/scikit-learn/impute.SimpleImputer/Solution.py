import numpy as np
from sklearn.impute import SimpleImputer

# Sample data with missing values
data = np.array([[1, 2, np.nan],
                 [3, np.nan, 4],
                 [7, 8, 9]])

# Initialize the imputer with the strategy 'mean'
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data
imputed_data = imputer.fit_transform(data)

print(imputed_data)
