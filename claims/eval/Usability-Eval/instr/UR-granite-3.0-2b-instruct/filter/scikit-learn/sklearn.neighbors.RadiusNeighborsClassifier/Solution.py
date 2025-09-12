from sklearn.neighbors import NearestNeighbors
from sklearn.base import BaseEstimator, ClassifierMixin

class VotingClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, estimators, n_neighbors=1):
        self.estimators = estimators
        self.n_neighbors = n_neighbors

    def fit(self, X, y):
        for estimator in self.estimators:
            estimator.fit(X, y)
        return self

    def predict(self, X):
        y_pred = []
        for estimator in self.estimators:
            distances, indices = estimator.kneighbors(X)
            votes = [self.estimators[i].predict(X[indices[i]]) for i in range(len(distances))]
            y_pred.append(max(set(votes), key=votes.count))
        return y_pred

    def predict_proba(self, X):
        y_probas = []
        for estimator in self.estimators:
            distances, indices = estimator.kneighbors(X)
            votes = [self.estimators[i].predict_proba(X[indices[i]]) for i in range(len(distances))]
            y_probas.append(max(set(votes), key=votes.count))
        return y_probas
