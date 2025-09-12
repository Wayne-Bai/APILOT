import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence

# Example dataset (replace this with your actual data)
from sklearn.datasets import fetch_california_housing
data, labels = fetch_california_housing(return_X_y=True)

# Create model
model = RandomForestRegressor(random_state=42)
model.fit(data, labels)

# Specify which features to plot the PDP for
features = [0, 2]  # Example: Aviable_housing

# Generate partial dependence plots
figure, axs = plt.subplots(1, 2, figsize=(14, 5))
plot_partial_dependence(model, data, features, ax=axs, grid_resolution=50)
