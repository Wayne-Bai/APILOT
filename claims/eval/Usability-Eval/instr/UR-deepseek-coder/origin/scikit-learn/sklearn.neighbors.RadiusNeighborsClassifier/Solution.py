from sklearn.neighbors import KNeighborsClassifier
from sklearn.base import BaseEstimator, ClassifierMixin
import numpy as np

class RadiusNeighborsClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, radius=1.0, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski'):
        self.radius = radius
        self.weights = weights
        self.algorithm = algorithm
        self.leaf_size = leaf_size
        self.p = p
        self.metric = metric
        self.knn = KNeighborsClassifier(n_neighbors=1, algorithm=algorithm, leaf_size=leaf_size, p=p, metric=metric)

    def fit(self, X, y):
        self.knn.fit(X, y)
        self.classes_ = self.knn.classes_
        return self

    def predict(self, X):
        y_pred = []
        for x in X:
            distances, indices = self.knn.kneighbors([x], n_neighbors=None, radius=self.radius)
            if len(indices[0]) == 0:
                y_pred.append(None)
            else:
                neighbors = self.knn._y[indices[0]]
                if self.weights == 'uniform':
                    votes = np.bincount(neighbors)
                else:
                    weights = np.exp(-distances[0])
                    votes = np.bincount(neighbors, weights=weights)
                y_pred.append(np.argmax(votes))
        return np.array(y_pred)

# Example usage:
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# iris = load_iris()
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
# clf = RadiusNeighborsClassifier(radius=1.0)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
