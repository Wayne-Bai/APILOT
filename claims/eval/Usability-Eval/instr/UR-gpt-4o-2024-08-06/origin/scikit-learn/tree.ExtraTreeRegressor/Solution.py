from sklearn.ensemble import ExtraTreesRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a synthetic regression dataset
X, y = make_regression(n_samples=100, n_features=4, noise=0.2, random_state=42)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the extremely randomized tree regressor
extra_tree_regressor = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Train the model
extra_tree_regressor.fit(X_train, y_train)

# Make predictions with the model
y_pred = extra_tree_regressor.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
