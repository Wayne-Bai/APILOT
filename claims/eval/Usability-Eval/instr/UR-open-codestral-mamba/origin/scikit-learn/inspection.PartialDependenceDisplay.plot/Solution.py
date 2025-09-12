
from sklearn.datasets import load_boston
from sklearn.inspection import plot_partial_dependence
from sklearn.inspection._partial_dependence import partial_dependence
from sklearn.ensemble import RandomForestRegressor

# Load Boston Housing dataset
boston = load_boston()

# Initialize the RandomForest model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Fit the model
model.fit(boston.data, boston.target)

# Specify which features to plot the partial dependence plots for
features = [2, (5, 9)]

# Plot
plot_partial_dependence(model, boston.data, features)
