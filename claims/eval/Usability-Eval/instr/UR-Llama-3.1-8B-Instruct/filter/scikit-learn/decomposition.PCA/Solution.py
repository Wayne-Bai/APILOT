# Import necessary libraries
from sklearn.decomposition import TruncatedSVD
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
iris = load_iris()

# Convert the dataset into a numpy array
X = iris.data

# Apply SVD for PCA
svd = TruncatedSVD(n_components=2, random_state=42)
X_pca = svd.fit_transform(X)

# Print the transformed data
print("Transformed data (2 components): \n", X_pca)

# Print the explained variance ratio
print("Explained variance ratio: \n", svd.explained_variance_ratio_)

# Print the singular values
print("Singular values: \n", svd.singular_values_)

# Print the number of features (which is the number of zero singular values)
print("Number of features (zero singular values): \n", svd.k_)
