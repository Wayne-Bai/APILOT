from sklearn.base import BaseEstimator, RegressorMixin

class RuleBasedRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, rule_value=0):
        self.rule_value = rule_value

    def fit(self, X, y=None):
        # No actual fitting is needed for this simple rule-based regressor
        return self

    def predict(self, X):
        # Apply the simple rule to make predictions
        return [self.rule_value] * len(X)

# Example usage:
import numpy as np

# Create a simple dataset
X = np.array([[1], [2], [3], [4]])
y = np.array([1, 2, 3, 4])

# Initialize the rule-based regressor with a rule value of 2
regressor = RuleBasedRegressor(rule_value=2)

# Fit the regressor (no actual fitting happens)
regressor.fit(X, y)

# Make predictions
predictions = regressor.predict(X)
print(predictions)  # Output: [2, 2, 2, 2]
