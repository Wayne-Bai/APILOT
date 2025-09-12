import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from scipy.sparse.csgraph import laplacian
from scipy.sparse.linalg import eigsh

# Generate some data
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Compute the normalized Laplacian
L = laplacian(X_scaled, normed=True)

# Compute the first k eigenvectors (k = number of clusters)
k = 2
eigenvalues, eigenvectors = eigsh(L, k + 1, which='SM', tol=1e-3)
projected_data = eigenvectors[:, 1:k+1]

# Apply KMeans to the projected data
kmeans = KMeans(n_clusters=k)
kmeans.fit(projected_data)
labels = kmeans.labels_

# Output the cluster labels
print(labels)
