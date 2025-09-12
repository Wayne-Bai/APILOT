from sklearn.decomposition import PCA
import numpy as np

# Assume X is your input data
X = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])

# Create a PCA object with n_components set to 1
pca = PCA(n_components=1)

# Fit and transform the data
X_transformed = pca.fit_transform(X)

# The transformed data is now in the lower dimensional space
print(X_transformed)
