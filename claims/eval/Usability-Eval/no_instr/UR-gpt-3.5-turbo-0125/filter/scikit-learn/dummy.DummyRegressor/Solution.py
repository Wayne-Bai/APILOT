
# Import the necessary libraries
import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin

# Define the class for the Regressor that makes predictions using simple rules
class SimpleRuleRegressor(BaseEstimator, RegressorMixin):
    
    def __init__(self, threshold=0.5):
        self.threshold = threshold
        
    def fit(self, X, y):
        self.threshold_value = np.mean(y)
        
    def predict(self, X):
        return [self.threshold_value if x > self.threshold else 0 for x in X]
