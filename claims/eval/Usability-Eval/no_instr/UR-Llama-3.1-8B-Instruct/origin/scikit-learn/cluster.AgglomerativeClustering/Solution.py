# Importing necessary libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the iris dataset
iris = load_iris()
data = iris.data
print("Original Data:\n", data)

# Reshape the data
data = np.array(data).reshape(-1, 5)

# Scale the data using StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Create an AgglomerativeClustering object with 3 clusters
agglomerative = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

# Fit the data to the clustering algorithm
agglomerative.fit(scaled_data)

# Predict the clusters
predicted_clusters = agglomerative.labels_

# Create a DataFrame with the original data and the predicted clusters
cluster_data = pd.DataFrame({
    'Sepal Length': iris.data[:, 0],
    'Sepal Width': iris.data[:, 1],
    'Petal Length': iris.data[:, 2],
    'Petal Width': iris.data[:, 3],
    'Cluster': predicted_clusters
})

# Print the DataFrame
print("Clustered Data:\n", cluster_data)

# Plot the clusters using 3D scatter plot
plt.figure(figsize=(10, 7))
plt.scatter(cluster_data['Sepal Length'], cluster_data['Sepal Width'], c=cluster_data['Cluster'])
plt.title('Agglomerative Clustering')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
