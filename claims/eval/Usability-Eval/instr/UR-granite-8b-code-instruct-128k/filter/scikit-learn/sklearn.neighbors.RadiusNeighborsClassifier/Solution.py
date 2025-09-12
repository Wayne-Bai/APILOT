from sklearn.neighbors import KNeighborsClassifier

class VoteNeighborsClassifier:
    def __init__(self, n_neighbors=5, radius=1.0):
        self.n_neighbors = n_neighbors
        self.radius = radius
        self.clf = KNeighborsClassifier(n_neighbors=self.n_neighbors, radius=self.radius)

    def fit(self, X, y):
        self.clf.fit(X, y)
        return self

    def predict(self, X):
        return self.clf.predict(X)
