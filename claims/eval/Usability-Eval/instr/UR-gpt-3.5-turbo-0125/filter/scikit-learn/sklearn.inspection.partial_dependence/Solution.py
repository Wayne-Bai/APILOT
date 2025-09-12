
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import load_boston

# Load the Boston housing dataset
data = load_boston()
X, y = data.data, data.target

# Create a GradientBoostingRegressor model
model = GradientBoostingRegressor()

# Fit the model
model.fit(X, y)

# Plot partial dependence of the 1st and 5th features against the target
features = [0, 4]  # Features for which partial dependence will be calculated
plot_partial_dependence(model, X, features, feature_names=data.feature_names)
