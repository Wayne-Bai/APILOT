from sklearn.metrics import pairwise_distances

# Assume we have two numpy arrays X and Y of equal size
X = [[1, 2], [3, 4]]
Y = [[1, 2], [1, 2]]

# Calculate L1 distances
distances = pairwise_distances(X, Y, metric='manhattan')

print(distances)
