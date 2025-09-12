
# Importing necessary libraries
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import load_boston

# Load the Boston housing dataset
X, y = load_boston(return_X_y=True)

# Fit a Gradient Boosting Regressor model
gbr = GradientBoostingRegressor(n_estimators=100, max_depth=4, learning_rate=0.1, random_state=0)
gbr.fit(X, y)

# Generate partial dependence plots
features = [5, (5, 7)]  # Example feature or feature pairs to plot partial dependence
fig, ax = plot_partial_dependence(gbr, X, features=features, feature_names=load_boston()['feature_names'])
