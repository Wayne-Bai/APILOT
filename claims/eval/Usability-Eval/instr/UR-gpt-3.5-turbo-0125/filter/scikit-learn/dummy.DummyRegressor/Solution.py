
# Import the necessary libraries
from sklearn.base import BaseEstimator, RegressorMixin
import numpy as np

# Create a custom regressor class
class SimpleRuleRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, threshold=0):
        self.threshold = threshold

    def fit(self, X, y=None):
        # No training involved for a simple rule regressor
        pass

    def predict(self, X):
        # Make predictions based on a simple rule
        predictions = np.where(X <= self.threshold, 0, 1)
        return predictions
