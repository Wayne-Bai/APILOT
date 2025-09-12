
import numpy as np
from sklearn.impute import SimpleImputer

# Assuming 'X' is your dataset
# Create the SimpleImputer object with strategy as 'mean', 'median', 'most_frequent', or 'constant'
imputer = SimpleImputer(strategy='mean')  # Other options: strategy='median', strategy='most_frequent', strategy='constant', fill_value=0

# Fit the imputer to the dataset 'X'
imputer.fit(X)

# Transform and replace missing values in 'X'
X_imputed = imputer.transform(X)
