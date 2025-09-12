
from sklearn.cluster import KMeans
import pandas as pd

# Load dataset
df = pd.read_csv('data.csv')

# Create a KMeans model
kmeans = KMeans(n_clusters=3)

# Fit the data to the model
kmeans.fit(df)

# Get the cluster labels for each sample in X
labels = kmeans.predict(df)

# Print the cluster labels
print(labels)
