import numpy as np
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example dataset
X = np.random.rand(100, 10)  # 100 samples, 10 features
y = np.random.rand(100)      # 100 target values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Bayesian Ridge model
bayesian_ridge = BayesianRidge()

# Fit the model to the training data
bayesian_ridge.fit(X_train, y_train)

# Predict on the test data
y_pred = bayesian_ridge.predict(X_test)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
