from sklearn.datasets import make_classification
from sklearn.feature_selection import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram

# Create a synthetic dataset
X, y = make_classification(n_samples=100, n_features=10, random_state=42)

# Normalize features
X = (X - X.mean(axis=0)) / X.std(axis=0)

# Agglomerative clustering
n_clusters = 3
cluster = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')

# Fit the model and get the labels
cluster_labels = cluster.fit_predict(X.T)  # Transpose X to cluster features instead of samples

# Function to append cluster labels in names
def append_cluster_label(labels, prefix='Feature'):
    return [f"{prefix}{i}_Cluster{label}" for i, label in enumerate(labels, 1)]

# Create a dendrogram
def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram
    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

# Create plotting values
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X.T)
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(model, labels=append_cluster_label(cluster_labels))
plt.show()
