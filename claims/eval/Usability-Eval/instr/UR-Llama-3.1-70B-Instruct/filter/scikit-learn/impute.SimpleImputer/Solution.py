# Import necessary libraries
from sklearn.impute import SimpleImputer
from sklearn.impute import IterativeImputer
import numpy as np

# Create a sample dataset with missing values
X = np.array([[1, 2], [np.nan, 3], [7, 6]])

# Using mean strategy
imputer_mean = SimpleImputer(strategy='mean') 
imputer_mean.fit(X)
X_mean_imputed = imputer_mean.transform(X)
print("Imputed data using mean strategy: \n", X_mean_imputed)

# Using median strategy
imputer_median = SimpleImputer(strategy='median') 
imputer_median.fit(X)
X_median_imputed = imputer_median.transform(X)
print("Imputed data using median strategy: \n", X_median_imputed)

# Using most_frequent strategy
imputer_most_frequent = SimpleImputer(strategy='most_frequent') 
imputer_most_frequent.fit(X)
X_most_frequent_imputed = imputer_most_frequent.transform(X)
print("Imputed data using most_frequent strategy: \n", X_most_frequent_imputed)

# Using constant strategy
imputer_constant = SimpleImputer(strategy='constant', fill_value=5) 
imputer_constant.fit(X)
X_constant_imputed = imputer_constant.transform(X)
print("Imputed data using constant strategy: \n", X_constant_imputed)
