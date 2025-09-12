from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Assume X is your normalized Laplacian data

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA to reduce dimensionality
pca = PCA(n_components=0.95)  # Keep 95% of the variation
X_pca = pca.fit_transform(X_scaled)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # Change the number of clusters as needed
kmeans.fit(X_pca)

# Get cluster labels
labels = kmeans.labels_
