from sklearn.base import RegressorMixin, BaseEstimator
import numpy as np

class SimpleRuleRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, threshold=0.5):
        self.threshold = threshold

    def fit(self, X, y):
        return self

    def predict(self, X):
        # Make a simple rule-based prediction
        # Here, we take the mean as a simplistic rule
        return np.where(X > self.threshold, X.mean(), self.threshold)
