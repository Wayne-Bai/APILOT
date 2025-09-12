from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Simulated data: an array with samples and features
# Example: 10 samples with 5 features each
data = np.random.rand(10, 5)

# Creating an instance of AgglomerativeClustering
# Here, we are setting the number of clusters to 3
agglomerative = AgglomerativeClustering(n_clusters=3)

# Fit model
clusters = agglomerative.fit_predict(data)

print("Cluster assignments:", clusters)
