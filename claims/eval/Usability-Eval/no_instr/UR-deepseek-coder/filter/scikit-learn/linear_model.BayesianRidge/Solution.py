import numpy as np
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 10)
true_weights = np.random.randn(10)
noise = np.random.randn(100) * 0.5
y = X.dot(true_weights) + noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize the Bayesian Ridge Regression model
bayesian_ridge = BayesianRidge(compute_score=True)

# Fit the model to the training data
bayesian_ridge.fit(X_train, y_train)

# Predict on the test data
y_pred = bayesian_ridge.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Access the learned parameters
print(f"Learned weights: {bayesian_ridge.coef_}")
print(f"Learned intercept: {bayesian_ridge.intercept_}")
print(f"Learned alpha: {bayesian_ridge.alpha_}")
print(f"Learned lambda (lambda_1 and lambda_2): {bayesian_ridge.lambda_}")
