from sklearn.cluster import KMeans
import numpy as np

# Assuming X is your data and n_clusters is the number of clusters you want to form
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
