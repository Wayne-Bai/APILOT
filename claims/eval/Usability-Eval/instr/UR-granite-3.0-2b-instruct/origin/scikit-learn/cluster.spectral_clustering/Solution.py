from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer
import numpy as np

# Assuming X is your data
Normalizer = Normalizer(copy=True, norm='l2')
X_normalized = Normalizer().fit_transform(X)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_normalized)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_pca)

# Get the cluster labels
labels = kmeans.labels_
