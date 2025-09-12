from sklearn.cluster import KMeans
import numpy as np

# Assuming X is your feature matrix
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.predict(X)
