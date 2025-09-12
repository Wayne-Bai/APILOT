import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import pairwise_distances
from collections import Counter

class CustomRadiusNeighborsClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, radius=1.0):
        self.radius = radius

    def fit(self, X, y):
        self.X_train_ = X
        self.y_train_ = y
        return self

    def predict(self, X):
        y_pred = []
        for x in X:
            neighbors_idxs = self._find_neighbors(x)
            if len(neighbors_idxs) == 0:
                # No neighbors, returning a default value,
                # here assuming binary classification with labels 0 or 1
                y_pred.append(0)
            else:
                neighbor_labels = self.y_train_[neighbors_idxs]
                most_common_label = Counter(neighbor_labels).most_common(1)[0][0]
                y_pred.append(most_common_label)
        return np.array(y_pred)
    
    def _find_neighbors(self, x):
        distances = pairwise_distances(self.X_train_, [x])
        # Find indices of neighbors within the given radius
        neighbors_idxs = np.where(distances <= self.radius)[0]
        return neighbors_idxs

# Example usage:
# X_train = np.array([[1, 1], [2, 2], [3, 3]])
# y_train = np.array([0, 1, 1])
# X_test = np.array([[1.5, 1.5], [2.5, 2.5]])

# clf = CustomRadiusNeighborsClassifier(radius=1.0)
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
# print(predictions)
