
from sklearn.cluster import KMeans

# Assuming X is your data

# Create KMeans model
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the model on your data X
kmeans.fit(X)

# Predict the closest cluster for each sample in X
closest_clusters = kmeans.predict(X)

print(closest_clusters)
