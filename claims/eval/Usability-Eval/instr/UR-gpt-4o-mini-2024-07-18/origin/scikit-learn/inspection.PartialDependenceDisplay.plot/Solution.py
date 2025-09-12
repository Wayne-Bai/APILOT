import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.model_selection import train_test_split

# Load the California housing dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a Gradient Boosting model
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_train)

# Create partial dependence plots
features = [0, 1]  # Selecting the first two features for demonstration
fig, ax = plt.subplots(figsize=(12, 6))
plot_partial_dependence(model, X_train, features, ax=ax, grid_resolution=50)

plt.show()
