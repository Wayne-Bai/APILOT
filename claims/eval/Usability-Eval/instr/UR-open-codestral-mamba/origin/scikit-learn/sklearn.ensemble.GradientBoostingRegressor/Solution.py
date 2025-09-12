from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate a random regression problem
X, y = make_regression(n_samples=100, n_features=100, noise=0.1)

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Gradient Boosting Regressor
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42)

# Fit the model to the training data
gbr.fit(X_train, y_train)

# Predict the results for the test data
y_pred = gbr.predict(X_test)

y_pred
