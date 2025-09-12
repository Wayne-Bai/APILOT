from sklearn.cluster import MiniBatchKMeans
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

# Load iris dataset
iris = datasets.load_iris()
features = iris.data

# Standardize the features to have zero mean and unit variance
scaler = StandardScaler().fit(features)
features_std = scaler.transform(features)

# Apply MiniBatchKMeans clustering
kmeans = MiniBatchKMeans(n_clusters=3, random_state=0).fit(features_std)
