from sklearn.base import BaseEstimator, RegressorMixin

class RuleBasedRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, rule_func):
        self.rule_func = rule_func

    def fit(self, X, y=None):
        # No actual fitting is needed for rule-based regressors
        return self

    def predict(self, X):
        return self.rule_func(X)

# Example rule function
def example_rule(X):
    return X[:, 0] * 2 + X[:, 1] * 3

# Usage
import numpy as np

# Generate some sample data
X_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([8, 18, 28])

# Create and fit the regressor
regressor = RuleBasedRegressor(rule_func=example_rule)
regressor.fit(X_train, y_train)

# Make predictions
X_test = np.array([[7, 8], [9, 10]])
predictions = regressor.predict(X_test)
print(predictions)
