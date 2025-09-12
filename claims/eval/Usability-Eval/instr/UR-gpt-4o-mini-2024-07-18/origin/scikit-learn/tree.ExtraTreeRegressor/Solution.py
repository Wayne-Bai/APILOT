from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import numpy as np

# Generate a synthetic regression dataset
X, y = make_regression(n_samples=100, n_features=20, noise=0.1, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an Extremely Randomized Trees Regressor
etr_regressor = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the regressor to the training data
etr_regressor.fit(X_train, y_train)

# Predict on the testing set
y_pred = etr_regressor.predict(X_test)

# Output predictions
print(y_pred)
