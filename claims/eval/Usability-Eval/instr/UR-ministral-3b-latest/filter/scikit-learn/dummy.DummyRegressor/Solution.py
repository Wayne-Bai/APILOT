from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.base import BaseEstimator
from sklearn.metrics import mean_squared_error

class SimpleRulesRegression(BaseEstimator):
    def __init__(self, rules=None):
        self.rules = rules

    def fit(self, X, y):
        # Implementation of your simple rule-based fitting logic
        # Using sklearn's fit method is discouraged due to API deprecation
        for rule in self.rules:
            feature_value, rule_value = rule
            X_selected = (X == feature_value).astype(int) * rule_value
            X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)
            regr = LinearRegression()
            regr.fit(X_train, y_train)
            y_pred = regr.predict(X_test)

        return self

    def predict(self, X):
        # Generate predictions based on your simple rules
        y_pred = []
        for rule in self.rules:
            feature_value, rule_value = rule
            X_selected = (X == feature_value).astype(int) * rule_value
            y_pred_single = LinearRegression().predict(X_selected)
            y_pred.append(y_pred_single)

        return sum(y_pred)

# Example usage
data = [
    [[0, 2], 3],  # Pre-white cab
    [[0, 3], 5],  # Place-orders
    [[0, 4], 0],  # Not processed
    [[1, 2], 8],  # Medical
    [[1, 3], 6],  # Red
    [[1, 4], 2],  # Black
]

X = [row[0] for row in data]
y = [row[1] for row in data]
rules = [[i, rule_value] for i, rule_value in zip([0, 1], [2, 0])]
model = SimpleRulesRegression(rules=rules)

model.fit(X, y)
predictions = model.predict(X)
print(predictions)
