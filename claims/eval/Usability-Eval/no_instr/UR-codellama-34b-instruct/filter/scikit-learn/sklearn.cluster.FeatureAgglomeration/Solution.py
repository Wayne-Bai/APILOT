from sklearn.cluster import AgglomerativeClustering

# Create a dataset with some sample data
X = [[1, 2], [2, 3], [3, 4], [4, 5]]

# Define the linkage criterion to use for merging clusters
linkage = 'ward'

# Create an AgglomerativeClustering object and fit it to the data
clusterer = AgglomerativeClustering(linkage=linkage)
clusterer.fit(X)

# Print the resulting clusters
print("Agglomerated clusters:")
for i, cluster in enumerate(clusterer.labels_):
    print(f"Cluster {i}:", cluster)
