# Import necessary libraries from scikit-learn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the ExtraTreesRegressor
extra_trees_regressor = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Fit the model on the training data
extra_trees_regressor.fit(X_train, y_train)

# Predict on the test data
y_pred = extra_trees_regressor.predict(X_test)

# Evaluate the model performance using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
