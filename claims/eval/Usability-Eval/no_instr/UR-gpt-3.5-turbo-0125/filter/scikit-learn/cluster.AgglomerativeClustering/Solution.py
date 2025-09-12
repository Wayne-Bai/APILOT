
# Importing the necessary library
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram

# Generating sample data
X = np.array([[1, 2], [1, 4], [1, 0],
               [4, 2], [4, 4], [4, 0]])

# Perform Agglomerative Clustering
Z = linkage(X, 'single')

# Plotting the dendrogram
dendrogram(Z)

