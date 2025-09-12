import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Create a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the GradientBoostingRegressor
regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the model
regressor.fit(X_train, y_train)

# Predict using the model
predictions = regressor.predict(X_test)

# Optional: Evaluate the model
print("Model accuracy on test set:", regressor.score(X_test, y_test))
