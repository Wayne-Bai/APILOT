
from sklearn.base import BaseEstimator

class SubEstimatorDecorator(BaseEstimator):
    def __init__(self, estimator):
        self.estimator = estimator

    def fit(self, X, y=None):
        return self.estimator.fit(X, y)

    def predict(self, X):
        return self.estimator.predict(X)

    def score(self, X, y=None):
        return self.estimator.score(X, y)
