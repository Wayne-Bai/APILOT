import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.inspection import PartialDependenceDisplay

# Load the California housing dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Train a HistGradientBoostingRegressor model
model = HistGradientBoostingRegressor()
model.fit(X, y)

# Plot partial dependence plots for the first two features
features = [0, 1]
PartialDependenceDisplay.from_estimator(model, X, features)
plt.show()
