from sklearn.impute import SimpleImputer
import numpy as np

# Create a sample dataset with missing values
X = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])

# Initialize the SimpleImputer with the 'mean' strategy
imputer = SimpleImputer(strategy='mean')

# Fit and transform the imputer on the dataset
X_imputed = imputer.fit_transform(X)

print("Original dataset:")
print(X)
print("\nImputed dataset:")
print(X_imputed)
