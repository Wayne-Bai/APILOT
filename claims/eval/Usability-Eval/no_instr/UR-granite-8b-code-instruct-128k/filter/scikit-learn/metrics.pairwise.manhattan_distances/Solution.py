from sklearn.metrics import pairwise_distances

X = [[1, 2, 3], [4, 5, 6]]
Y = [[7, 8, 9], [10, 11, 12]]

l1_distances = pairwise_distances(X, Y, metric='manhattan')

print(l1_distances)
