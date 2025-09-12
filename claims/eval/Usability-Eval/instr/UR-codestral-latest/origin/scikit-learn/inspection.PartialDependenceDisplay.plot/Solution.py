import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay
import matplotlib.pyplot as plt

# Load California Housing dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Define the model
model = GradientBoostingRegressor()

# Fit the model
model.fit(X, y)

# Calculate and display the partial dependencies
features = [0, 1]  # let's say we're interested in the first two features
fig, ax = plt.subplots(figsize=(8, 6))
display = PartialDependenceDisplay.from_estimator(model, X, features)

# Show the plot
plt.show()
