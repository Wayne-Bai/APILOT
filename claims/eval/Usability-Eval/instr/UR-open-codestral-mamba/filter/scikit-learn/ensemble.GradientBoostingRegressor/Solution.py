# Import the necessary libraries
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import make_friedman1
from sklearn.metrics import mean_squared_error

# Generating a random n-dimensional regression problem
X, y = make_friedman1()

# Splitting the dataset into a training and testing set
X_train, X_test = X[:500], X[500:]
y_train, y_test = y[:500], y[500:]

# Initialize the Gradient Boosting Regressor
gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)

# Fit the model to the training data
gb.fit(X_train, y_train)

# Predict the y values for the test set
y_pred = gb.predict(X_test)

# Calculating the mean squared error of the predicted values
mse = mean_squared_error(y_test, y_pred)

mse
