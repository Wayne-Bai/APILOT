import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, RegressorMixin

# Simple regression model using rules
class SimpleRuleBasedRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, threshold=0.5, higher_value=1.0):
        self.threshold = threshold
        self.higher_value = higher_value

    def fit(self, X, y):
        # Here we can train a very simple rule-based model
        # For example we will use threshold to make predictions
        self.threshold = np.median(y)
        self.higher_value = np.min(y) if np.min(y) > 0 else 1.0
        return self

    def predict(self, X):
        y_pred = np.zeros_like(X)
        y_pred[X >= self.threshold] = self.higher_value
        return y_pred

# Example usage
np.random.seed(42)
X, y = make_regression(n_samples=10, n_features=1, noise=0.1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Create an instance of the SimpleRuleBasedRegressor
simple_regressor = SimpleRuleBasedRegressor()
simple_regressor.fit(X_train, y_train)

# Make predictions
y_pred = simple_regressor.predict(X_test)

# Print predictions
print(y_pred)
