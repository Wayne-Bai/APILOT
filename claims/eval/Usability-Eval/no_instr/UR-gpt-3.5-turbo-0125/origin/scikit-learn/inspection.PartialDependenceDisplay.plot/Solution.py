
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble.partial_dependence import plot_partial_dependence

# Create a sample dataset
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])

# Fit a GradientBoostingRegressor model
model = GradientBoostingRegressor()
model.fit(X, y)

# Plot partial dependence plots
features = [0, 1]  # Features for which partial dependence will be plotted
plot_partial_dependence(model, X, features)
plt.show()
