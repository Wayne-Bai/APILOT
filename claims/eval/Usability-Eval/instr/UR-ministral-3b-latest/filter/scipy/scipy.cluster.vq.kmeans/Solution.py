from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import linkage
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
observations = np.array([[1, 2], [1, 3], [1, 4], [5, 3], [5, 4], [5, 5], [1, 4], [1, 6], [2, 2], [2, 6], [4, 4], [4, 6]])

# Use completed-linkage to create a tree
Z = linkage(observations, 'complete')  # change 'complete' to 'median', 'average', 'ward', etc. for different linkage criteria

# Plot the dendrogram
f = plt.figure(figsize=(8, 8))
plt.title('Full-length dendrogram')
dendrogram(Z, truncate_mode='level', p=5)
plt.show()
