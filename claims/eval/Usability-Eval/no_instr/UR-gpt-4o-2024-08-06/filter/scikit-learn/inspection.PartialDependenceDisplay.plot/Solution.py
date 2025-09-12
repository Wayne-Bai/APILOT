import numpy as np
import matplotlib.pyplot as plt
from sklearn.inspection import PartialDependenceDisplay
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

# Load a dataset
california_housing = fetch_california_housing()
X, y = california_housing.data, california_housing.target
feature_names = california_housing.feature_names

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a model
model = GradientBoostingRegressor(n_estimators=100, max_depth=4, random_state=0)
model.fit(X_train, y_train)

# Define features for which to plot partial dependence
features = [0, 1, (0, 1)]  # Features 0 and 1, and a pair interaction (0, 1)

# Plot partial dependence
fig, ax = plt.subplots(figsize=(12, 8))
PartialDependenceDisplay.from_estimator(model, X_train, features, feature_names=feature_names, ax=ax)
plt.show()
