from scipy.cluster.vq import kmeans

# Insert your observation vectors and number of clusters here
observation_vectors = [[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]]
k = 2

centroids, distortion = kmeans(observation_vectors, k)

print("Centroids:", centroids)
print("Distortion:", distortion)
