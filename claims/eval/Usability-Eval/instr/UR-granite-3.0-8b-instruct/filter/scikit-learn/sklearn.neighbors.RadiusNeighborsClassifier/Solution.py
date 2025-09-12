from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.base import BaseEstimator, ClassifierMixin

class RadiusNeighborsClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, n_neighbors=5, weights='distance', algorithm='auto', leaf_size=30, p=2, radius=1.0):
        self.n_neighbors = n_neighbors
        self.weights = weights
        self.algorithm = algorithm
        self.leaf_size = leaf_size
        self.p = p
        self.radius = radius

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
        return self

    def predict(self, X):
        dists = euclidean_distances(X, self.X_train, squared=True)
        within_radius = dists < self.radius**2

        if not within_radius.any():
            return np.array([])

        neighbors = self.X_train[within_radius]
        votes = np.zeros(self.y_train.shape[0])
        for i in range(neighbors.shape[0]):
            votes[self.y_train[within_radius[i]]] += 1

        return np.argmax(votes)
