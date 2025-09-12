from sklearn.impute import KNNImputer
import numpy as np

# Example dataset with missing values
data = np.array([[1, 2, np.nan, 4],
                 [5, np.nan, 6, 8],
                 [9, 10, 11, 12],
                 [np.nan, 14, 15, np.nan]])

# Create KNNImputer instance with a number of neighbors
imputer = KNNImputer(n_neighbors=2, weights="uniform")

# Fit and transform the dataset
imputed_data = imputer.fit_transform(data)

print("Original Data:\n", data)
print("Imputed Data:\n", imputed_data)
