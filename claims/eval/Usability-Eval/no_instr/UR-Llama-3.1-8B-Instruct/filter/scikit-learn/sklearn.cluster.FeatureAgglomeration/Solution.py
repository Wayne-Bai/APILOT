from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Generate sample data
X, _ = make_blobs(n_samples=1000, n_features=4, centers=6, n_clusters=6, random_state=42)

# Create a DataFrame
df = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4'])

# Use AgglomerativeClustering to cluster features
agglo_clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='complete')
clusters = agglo_clustering.fit_predict(X)

# Create a DataFrame with clusters
df['Cluster'] = clusters

# Pivot the DataFrame to see the cluster assignments for each feature
feature_hz_pivot = pd.pivot_table(df, values='Cluster', columns='Feature', index=None, aggfunc='count', fill_value=0)
print(feature_hz_pivot)
