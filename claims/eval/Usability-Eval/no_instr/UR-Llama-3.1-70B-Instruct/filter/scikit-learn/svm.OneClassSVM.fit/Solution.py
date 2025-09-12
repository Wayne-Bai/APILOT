# Import necessary libraries
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA

# Create a sample dataset
X, _ = make_blobs(n_samples=200, centers=4, cluster_std=0.8, random_state=0)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Detect the soft boundary of the set of samples X using Gaussian Mixture Model
gmm = GaussianMixture(n_components=4, random_state=0)
gmm.fit(X)

# Predict the probability of each sample belonging to each cluster
probabilities = gmm.predict_proba(X)

# Get the cluster labels for each sample
labels = gmm.predict(X)

# Plot the clusters using PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.title("Gaussian Mixture Model Clustering")
plt.show()

# Plot the probability of each sample belonging to the first cluster
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=probabilities[:, 0], cmap='viridis')
plt.title("Soft Boundary of the First Cluster")
plt.show()
