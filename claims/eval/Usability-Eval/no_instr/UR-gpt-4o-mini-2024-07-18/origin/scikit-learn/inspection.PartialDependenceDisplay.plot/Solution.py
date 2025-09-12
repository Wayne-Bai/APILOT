import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.inspection import plot_partial_dependence

# Create a synthetic dataset
X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor()
model.fit(X, y)

# Plot partial dependence for the first two features
features = [0, 1]
fig, ax = plt.subplots(figsize=(12, 6))
plot_partial_dependence(model, X, features, ax=ax, grid_resolution=50)

plt.title('Partial Dependence Plot')
plt.show()
