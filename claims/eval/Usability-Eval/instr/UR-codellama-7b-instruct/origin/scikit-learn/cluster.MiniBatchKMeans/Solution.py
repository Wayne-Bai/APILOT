
import numpy as np
from sklearn.cluster import KMeans

# Load dataset
X = np.loadtxt('data.csv', delimiter=',')

# Initialize K-Means with Mini-Batch parameter set to True
kmeans = KMeans(n_clusters=5, random_state=42, batch_size=20).fit(X)
