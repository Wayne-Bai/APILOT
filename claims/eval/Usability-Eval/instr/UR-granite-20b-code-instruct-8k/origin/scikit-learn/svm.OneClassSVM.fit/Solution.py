from sklearn.cluster import DBSCAN

# Assuming you have your data stored in a variable called 'X'
# Initialize the DBSCAN model
dbscan = DBSCAN(eps=0.3, min_samples=5)

# Fit the model to your data
dbscan.fit(X)

# Get the labels of each sample
labels = dbscan.labels_

# Print the unique labels
unique_labels = set(labels)
print(unique_labels)
