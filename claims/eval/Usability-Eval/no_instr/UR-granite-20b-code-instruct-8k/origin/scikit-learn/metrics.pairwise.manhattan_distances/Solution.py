import sklearn

X = [[0, 1], [1, 1]]
Y = [[0, 1], [1, 0]]

l1_distances = sklearn.metrics.pairwise.manhattan_distances(X, Y)

print(l1_distances)
