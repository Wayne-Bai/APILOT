import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.inspection import plot_partial_dependence

# Create a synthetic dataset
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

# Fit a Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Create partial dependence plots
features = [0, 1]  # Replace with the feature indices you want to analyze
fig, ax = plt.subplots(figsize=(12, 6))
plot_partial_dependence(model, X, features, ax=ax)
plt.show()
