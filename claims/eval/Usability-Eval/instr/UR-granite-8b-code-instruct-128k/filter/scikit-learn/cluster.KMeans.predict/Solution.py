import sklearn
from sklearn.cluster import KMeans

# Assuming X is your data
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
