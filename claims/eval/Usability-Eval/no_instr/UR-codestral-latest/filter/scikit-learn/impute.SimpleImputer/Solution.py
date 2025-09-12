from sklearn.impute import SimpleImputer
import numpy as np

# Let's consider the following numpy array with missing values (represented by np.nan)
X = np.array([[1, 2], [np.nan, 3], [7, 6]])

# Use SimpleImputer for mean strategy
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# Fit and transform the data
X_imputed = imputer.fit_transform(X)

print(X_imputed)
