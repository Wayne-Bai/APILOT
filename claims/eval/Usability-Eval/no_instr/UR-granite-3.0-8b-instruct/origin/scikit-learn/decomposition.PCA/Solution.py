from sklearn.decomposition import PCA
import numpy as np

# Assuming X is your input data
X = np.array([[1, 2], [3, 4], [5, 6]])

# Initialize PCA
pca = PCA()

# Fit and transform the data
X_pca = pca.fit_transform(X)

print(X_pca)
