from sklearn.decomposition import SparsePCA
from sklearn.datasets import make_sparse_coded_signal
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate a sparse encoded signal
X, _ = make_sparse_coded_signal(n_samples=1000, n_features=100, n_components=10, random_state=42)

# Initialize SparsePCA with alpha=0.1
spca = SparsePCA(n_components=10, alpha=0.1, random_state=42)

# Fit the model to the data
spca.fit(X)

# Transform the data
X_transformed = spca.transform(X)

# Calculate the mean squared error of the reconstruction
mse = mean_squared_error(X, spca.inverse_transform(X_transformed))

print(f"Mean Squared Error: {mse}")
