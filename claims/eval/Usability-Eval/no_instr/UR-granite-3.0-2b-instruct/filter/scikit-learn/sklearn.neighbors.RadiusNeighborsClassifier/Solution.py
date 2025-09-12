from sklearn.neighbors import NearestNeighbors
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_X_y
from sklearn.utils.validation import check_array

class NeighborhoodClassifier(BaseEstimator, TransformerMixin):
    def __init__(self, n_neighbors=5, weights='distance', algorithm='auto', leaf_size=30, p=2, metric='euclidean'):
        self.nbrs = NearestNeighbors(n_neighbors=n_neighbors, weights=weights, algorithm=algorithm, leaf_size=leaf_size, p=p, metric=metric)
        self.classes_ = []

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.nbrs.fit(X)
        self.classes_ = [y.mode()[0]] * len(y)
        return self

    def predict(self, X):
        X = check_array(X)
        dists, indices = self.nbrs.kneighbors(X)
        votes = self.classes_[indices]
        return votes.mode(axis=1).mode()[0]
