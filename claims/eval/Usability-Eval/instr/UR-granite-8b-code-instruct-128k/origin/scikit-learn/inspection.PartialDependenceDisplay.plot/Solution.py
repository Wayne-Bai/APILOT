
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence

# Load the Boston dataset
boston = load_boston()

# Create a Random Forest model
model = RandomForestRegressor()

# Fit the model to the data
model.fit(boston.data, boston.target)

# Plot partial dependence plots
plot_partial_dependence(model, boston.data, [0, 1, 2])
