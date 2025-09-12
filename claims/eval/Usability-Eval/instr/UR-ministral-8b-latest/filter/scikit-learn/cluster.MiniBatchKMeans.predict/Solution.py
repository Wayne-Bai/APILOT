import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Assuming X is the input data and its shape should be (n_samples, n_features)
X = np.array([
    [2.0, 3.0, 1.5],
    [1.5, 2.5, 1.0],
    [2.0, 4.5, 2.0],
    [3.0, 4.5, 3.0],
    [1.0, 3.5, 2.0]
])

# Standardize the data for better clustering performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA to reduce the dimensionality if necessary (Optional, depends on your dataset)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Perform K-Means Clustering
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_pca)

# Predict the closest cluster for each sample in X
clusters = kmeans.predict(X_pca)

print(clusters)  # Output will be an array with cluster labels for each sample
