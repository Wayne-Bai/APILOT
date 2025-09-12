from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the iris dataset
data = load_iris()
X = data.data

# Create a PCA that will retain 99% of variance
pca = PCA(n_components=0.99, whiten=True)

# Conduct PCA
data = pca.fit_transform(X)

# Transform data back to its original space
data_transformed = pca.inverse_transform(data)

# Check shape of original and transformed data
print(f"Original shape: {X.shape}, transformed shape: {data_transformed.shape}")
