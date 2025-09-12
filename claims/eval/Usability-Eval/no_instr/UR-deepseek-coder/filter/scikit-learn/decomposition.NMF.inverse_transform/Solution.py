from sklearn.decomposition import PCA
import numpy as np

# Assuming X_transformed is the transformed data and pca is the PCA object used for transformation

# Example data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pca = PCA(n_components=2)
X_transformed = pca.fit_transform(X)

# Transform data back to its original space
X_original = pca.inverse_transform(X_transformed)

print("Original data:\n", X)
print("Transformed data:\n", X_transformed)
print("Data back to original space:\n", X_original)
