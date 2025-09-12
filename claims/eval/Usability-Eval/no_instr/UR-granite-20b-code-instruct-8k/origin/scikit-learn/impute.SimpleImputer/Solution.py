from sklearn.impute import SimpleImputer
import numpy as np

# Create a sample array with missing values
X = np.array([[1, 2], [np.nan, 3], [4, 5]])

# Create an instance of the UnivariateImputer class with the strategy set to 'mean'
imputer = SimpleImputer(strategy='mean')

# Fit and transform the array to replace missing values
X_imputed = imputer.fit_transform(X)

# Print the imputed array
print(X_imputed)
