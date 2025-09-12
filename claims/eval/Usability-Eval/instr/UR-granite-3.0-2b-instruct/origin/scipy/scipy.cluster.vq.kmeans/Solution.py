from scipy.cluster.vq import kmeans, vq
import numpy as np

# Generate some random data
data = np.random.rand(100, 2)

# Choose the number of clusters
k = 3

# Perform k-means clustering
编码, 距离 = kmeans(data, k)

# Visualize the clusters (if possible)
# ...

# Verify the clustering by performing vector quantization
编码, 距离 = vq(data, 编码)
