# Importing necessary libraries from scikit-learn
from sklearn.cluster import KMeans
from sklearn.datasets import make_moons
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
X, y = make_moons(n_samples=200, noise=.05, random_state=0)

# Reshape data to 2D numpy array (if needed)
X = X.reshape(-1, 2)

# Reshape data if shape is not 2D
X = np.array(X).reshape(-1, 2)

# Create a KMeans model with 2 clusters (default)
kmeans = KMeans(n_clusters=2)

# Fit model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
y_pred = kmeans.predict(X)

# Print cluster labels
print(y_pred)

# Plot the data with predicted clusters
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
