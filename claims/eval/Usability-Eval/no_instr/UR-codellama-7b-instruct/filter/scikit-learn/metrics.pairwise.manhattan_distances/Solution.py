from sklearn.metrics.pairwise import manhattan_distance

# Example data
X = [[1, 2], [3, 4], [5, 6]]
Y = [[7, 8], [9, 10], [11, 12]]

# Compute the L1 distances between the vectors in X and Y
distances = manhattan_distance(X, Y)

print(distances)
