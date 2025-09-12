from sklearn.impute import SimpleImputer
import numpy as np

# Assume X is the input numpy array with missing values
X = np.array([[7, 2, 3], [4, np.nan, 6], [10, 5, 9], [1, 2, np.nan]])

# Create an instance of SimpleImputer class with strategy as mean
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data for univariate imputation
imputed_X = imputer.fit_transform(X)

print("Imputed data:")
print(imputed_X)
