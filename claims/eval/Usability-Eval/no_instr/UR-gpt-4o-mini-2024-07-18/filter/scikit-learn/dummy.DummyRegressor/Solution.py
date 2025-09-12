import numpy as np
from sklearn.base import BaseEstimator, RegressorMixin

class SimpleRuleRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, rule_type='mean'):
        self.rule_type = rule_type
        self.rule_value = None

    def fit(self, X, y):
        if self.rule_type == 'mean':
            self.rule_value = np.mean(y)
        elif self.rule_type == 'median':
            self.rule_value = np.median(y)
        # Add more rules as needed
        else:
            raise ValueError("Unsupported rule type. Use 'mean' or 'median'.")

        return self

    def predict(self, X):
        if self.rule_value is None:
            raise ValueError("The model has not been fitted yet.")
        return np.full(shape=(X.shape[0],), fill_value=self.rule_value)

# Example usage
if __name__ == "__main__":
    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 3, 5, 7, 11])

    model = SimpleRuleRegressor(rule_type='mean')
    model.fit(X, y)
    predictions = model.predict(X)

    print("Predictions:", predictions)
