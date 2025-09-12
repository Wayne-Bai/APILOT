# Import necessary libraries
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import partial_dependence, partial_dependence_plot
import matplotlib.pyplot as plt

# Load the California Housing dataset
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Create a random forest regressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# Create partial dependence plots
dependence, grid = partial_dependence(rf, X, ['MedInc',"AveOccup"] )

# Plot partial dependence
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
for i, feature in enumerate(['MedInc', 'AveOccup']):
    partial_dependence_plot(feature, dependence, grid, ax=axs[i])
    axs[i].set_title(f'Partial Dependence Plot for {feature}')
plt.show()
