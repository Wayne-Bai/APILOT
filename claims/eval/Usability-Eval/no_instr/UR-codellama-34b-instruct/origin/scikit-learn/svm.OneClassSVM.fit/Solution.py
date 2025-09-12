from sklearn.cluster import DBSCAN

# Initialize the DBSCAN algorithm with epsilon = 0.5 and minimum samples = 10
dbscan = DBSCAN(eps=0.5, min_samples=10)

# Fit the algorithm to the data
dbscan.fit(X)

# Get the cluster labels for each sample
labels = dbscan.labels_

# Get the soft boundary of the clusters
soft_boundary = dbscan.get_soft_boundary()
