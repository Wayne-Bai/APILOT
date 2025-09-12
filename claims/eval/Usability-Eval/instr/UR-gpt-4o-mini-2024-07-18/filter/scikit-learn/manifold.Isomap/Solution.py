from sklearn.manifold import Isomap
import numpy as np

# Sample data
X = np.random.rand(10, 3)  # 10 samples, 3 features

# Create an Isomap instance with a specified number of neighbors and dimensions
isomap = Isomap(n_neighbors=5, n_components=2)

# Fit and transform the data
X_embedding = isomap.fit_transform(X)

print("Original data shape:", X.shape)
print("Isomap embedded data shape:", X_embedding.shape)
print("Isomap embedded data:", X_embedding)
