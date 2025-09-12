from sklearn.metrics.pairwise import l1_distance

# Assuming X and Y are your input vectors
X = [[1, 2], [3, 4], [5, 6]]
Y = [[7, 8], [9, 10], [11, 12]]

# Compute L1 distances
distances = l1_distance(X, Y)

print(distances)
