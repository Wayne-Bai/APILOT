
from sklearn.cluster import AgglomerativeClustering

# Create an instance of AgglomerativeClustering
model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')

# Fit the model to your data
model.fit(data)

# Obtain the labels or cluster assignments
labels = model.labels_
