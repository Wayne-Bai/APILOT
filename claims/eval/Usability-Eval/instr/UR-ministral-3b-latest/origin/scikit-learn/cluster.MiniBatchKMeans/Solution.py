from sklearn.cluster import KMeans
import numpy as np

# Assume we have some data that needs clustering
data = np.random.rand(100, 2)  # 100 samples, 2 features each

# Instantiate the MiniBatchKMeans model
kmeans = KMeans(n_clusters=3, random_state=42, batch_size=32)

# Fit the model to the data
kmeans.fit(data)

# Predict the cluster for each sample
labels = kmeans.predict(data)

# Print the cluster labels for each sample
print(labels)
