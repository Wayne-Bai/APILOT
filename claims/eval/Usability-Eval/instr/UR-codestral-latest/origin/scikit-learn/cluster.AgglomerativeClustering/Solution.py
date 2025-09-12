from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Assume we have an array of sample data "X"
X = np.array(...)

# Create an Agglomerative Clustering model
clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=0)

# Fit the model to the data
clustering_model.fit(X)

# You can now use the model to predict the clusters of new data, for example:
# new_data = np.array(...)
# labels = clustering_model.fit_predict(new_data)
