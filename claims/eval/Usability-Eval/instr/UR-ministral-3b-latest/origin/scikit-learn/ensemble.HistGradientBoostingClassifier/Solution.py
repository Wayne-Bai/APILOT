from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import matplotlib.pyplot as plt

class HistogramGradientBoostingClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, n_estimators=10, learning_rate=1.0, max_depth=None):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_estimators):
            X_reduced = X.copy()
            y_reduced = y.copy()

            for tree in self.trees:
                X_reduced *= (1 - learning_rate)  # Reduce X by (1 - learning_rate)
                X_reduced += tree.tree_.y  # Add leaves from previous tree
                y_reduced = (y - y_reduced).clip(-1, 1)  # Clip targets to -1 and 1 for gradient boosting

            tree = GradientBoostingClassifier(learning_rate=self.learning_rate, max_depth=self.max_depth)
            tree.fit(X_reduced, y_reducted)
            self.trees.append(tree)

    def predict(self, X):
        predictions = np.zeros(X.shape[0])
        for tree in self.trees:
            predictions += tree.predict(X)  # Sum up predictions from each tree
        return np.round(predictions)  # Round to binary values (0, 1)

# Example usage
# from sklearn.datasets import make_classification
# X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# hist_gradient_boost = HistogramGradientBoostingClassifier(n_estimators=10, learning_rate=0.1)
# hist_gradient_boost.fit(X, y)
# y_pred = hist_gradient_boost.predict(X)
# accuracy = accuracy_score(y, y_pred)
# print('Accuracy:', accuracy)
