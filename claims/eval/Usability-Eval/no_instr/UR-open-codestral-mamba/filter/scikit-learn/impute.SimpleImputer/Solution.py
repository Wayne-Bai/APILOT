from sklearn.impute import SimpleImputer
import numpy as np

# Assume we have a 2-dimensional numpy array with missing values
X = np.array([[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 7], [8, 9, 10]])

# Initialize the SimpleImputer object
# strategy="mean" will replace missing values with the mean along each column
imputer = SimpleImputer(strategy="mean")

# Fit the imputer object to the data (i.e., compute the mean of each column)
imputer.fit(X)

# Transform the original data, replacing missing values with the computed means
X_imputed = imputer.transform(X)

print(X_imputed)
