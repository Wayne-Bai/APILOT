from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence
from sklearn.datasets import fetch_california_housing

# Load a dataset
dataset = fetch_california_housing()

# Build a Random Forest Regressor
model = RandomForestRegressor()
model.fit(dataset.data, dataset.target)

# plot partial dependence, specifying the average. Make sure to use features of interest.
# This example uses the first and second feature from the dataset.
features = [0, 1]
plot_partial_dependence(model, dataset.data, features)
