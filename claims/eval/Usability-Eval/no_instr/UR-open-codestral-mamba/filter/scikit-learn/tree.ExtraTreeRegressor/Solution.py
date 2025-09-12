from sklearn.ensemble import ExtraTreesRegressor
from sklearn.datasets import make_regression

# Generate a random regression problem
X, y = make_regression(n_samples=100, n_features=3, noise=0.5)

# Instantiate the ExtraTreesRegressor model
extra_tree_regressor = ExtraTreesRegressor(random_state=42)

# Fit the model with our randomly generated data
extra_tree_regressor.fit(X, y)

# Now we can predict values or use the model for other tasks
predictions = extra_tree_regressor.predict(X)
