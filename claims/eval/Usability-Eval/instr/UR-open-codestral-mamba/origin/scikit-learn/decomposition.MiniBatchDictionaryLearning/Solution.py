from sklearn.cluster import MiniBatchKMeans

# Assuming you have a 2D array X
X = [...] # your array here

# Create a MiniBatchKMeans object
kmeans = MiniBatchKMeans(n_clusters=3, random_state=0)

# Fit the data to the model
kmeans.fit(X)

# Display the cluster centers
print(kmeans.cluster_centers_)
