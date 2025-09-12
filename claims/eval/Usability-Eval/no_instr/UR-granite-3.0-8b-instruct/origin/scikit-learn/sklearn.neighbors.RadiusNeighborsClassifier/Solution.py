from sklearn.neighbors import NearestNeighbors
import numpy as np

class CustomKNeighborsClassifier:
    def __init__(self, n_neighbors, radius):
        self.n_neighbors = n_neighbors
        self.radius = radius
        self.model = NearestNeighbors(n_neighbors=n_neighbors, metric='euclidean')

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        predictions = []
        for point in X:
            distances, indices = self.model.kneighbors([point])
            neighbors = indices[0][:self.n_neighbors]
            neighbor_labels = self.model.labels_[neighbors]
            most_common = np.bincount(neighbor_labels).argmax()
            predictions.append(most_common)
        return np.array(predictions)
