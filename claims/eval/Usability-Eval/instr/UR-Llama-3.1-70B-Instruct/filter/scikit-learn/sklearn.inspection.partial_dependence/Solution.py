import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence, PartialDependenceDisplay

# Generate a random dataset
X = np.random.rand(1000, 3)
y = 10 * np.sin(np.pi * X[:, 0]) + 20 * np.cos(np.pi * X[:, 1]) + 10 * np.sin(np.pi * X[:, 2])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a gradient boosting regressor
gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train)

# Compute partial dependence
features = [0]
pd, axes = partial_dependence(gbr, X_train, features, grid_resolution=50)

# Create a PartialDependenceDisplay object
display = PartialDependenceDisplay(pd, features=features, feature_names=['Feature 1', 'Feature 2', 'Feature 3'], ax=axes)

# Plot the partial dependence for feature 1
plt.show()

# Compute and plot partial dependence for two features
features = [(0, 1)]
pd, axes = partial_dependence(gbr, X_train, features=features, grid_resolution=(50, 50))

display = PartialDependenceDisplay(pd, features=features, feature_names=['Feature 1', 'Feature 2', 'Feature 3'], ax=axes)
plt.show()
