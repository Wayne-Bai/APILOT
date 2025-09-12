from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler

# Assuming X is your data
# Normalize the data
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# Compute the Laplacian
L = X_normalized @ X_normalized.T - 2 * X_normalized.dot(X_normalized.mean(axis=0))

# Project the Laplacian
svd = TruncatedSVD(n_components=10)
X_projected = svd.fit_transform(L)

# Apply clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_projected)

# Print the cluster labels
print(kmeans.labels_)
