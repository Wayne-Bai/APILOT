from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Create an instance of the AgglomerativeClustering class
ac = AgglomerativeClustering(n_clusters=3)

# Fit the data to the model and get the labels for each sample
labels = ac.fit_predict(X)

# Print the cluster labels for each sample
print("Cluster labels:")
print(labels)
