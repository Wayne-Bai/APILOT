from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Sample data: 2D points
X = np.array([[1, 2],
              [1, 4],
              [1, 0],
              [4, 2],
              [4, 4],
              [4, 0]])

# Create an Agglomerative Clustering model 
# Define the number of clusters, linkage criteria is 'ward' by default
clustering_model = AgglomerativeClustering(n_clusters=2, linkage='ward')

# Fit the model and predict cluster labels
labels = clustering_model.fit_predict(X)

# Print the result
print("Cluster labels:", labels)
