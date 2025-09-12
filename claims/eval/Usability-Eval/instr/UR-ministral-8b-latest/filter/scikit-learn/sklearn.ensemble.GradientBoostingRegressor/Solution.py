import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor  # Note: This keeps the `GradientBoostingRegressor`
from sklearn.linear_model import LinearRegression
from functools import partial
from scipy.optimize import minimize

# Reload the Boston dataset, which is suitable for regression with Gradient Boosting
boston = load_boston()
X, y = boston.data, boston.target

# Split the dataset into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gradient Boosting Regressor with custom training loop
class CustomGradientBoostingRegressor:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        # Initial model
        self.trees.append(self.build_base_model(X, y))
        for _ in range(self.n_estimators - 1):
            # Compute the negative gradient (or residuals)
            residuals = y - self.predict(X)
            # Fit a tree to the residuals
            new_tree = self.build_tree(X, residuals)
            self.trees.append(new_tree)

    def predict(self, X):
        # Predict with the current ensemble of trees
        return sum(tree.predict(X) for tree in self.trees)

    def build_tree(self, X, y, max_depth=None):
        # Dummy tree building function for the example
        return LinearRegression()

    def build_base_model(self, X, y):
        # Base model using a linear regression (or another simple model)
       return LinearRegression()

    def score(self, X, y):
        # Calculate the mean squared error as a proxy for performance
        predictions = self.predict(X)
        return mean_squared_error(y, predictions)

# Create and train the Custom Gradient Boosting Regressor
gbr = CustomGradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
gbr.fit(X_train, y_train)

# Score the model on the test set
score = gbr.score(X_test, y_test)
print(f"Test Set Mean Squared Error: {score}")
