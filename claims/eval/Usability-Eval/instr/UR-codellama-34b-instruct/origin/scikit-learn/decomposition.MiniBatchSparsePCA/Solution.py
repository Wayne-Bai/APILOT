from sklearn.decomposition import SparsePCA
import numpy as np

# Generate some sample data
n_samples, n_features = 100, 50
np.random.seed(0)
X = np.random.randn(n_samples, n_features)

# Create a SparsePCA object and fit the data
spca = SparsePCA(n_components=5, alpha=0.1)
spca.fit(X)

# Get the transformed data
X_transformed = spca.transform(X)
