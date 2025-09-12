# Import necessary libraries
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error
import numpy as np

# Load diabetes dataset as an example
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an Extremely Randomized Tree Regressor
etr = ExtraTreesRegressor(n_estimators=100, random_state=42)

# Train the model using the training sets
etr.fit(X_train, y_train)

# Make predictions using the test set
y_pred = etr.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Model Parameters
print("Model Parameters:")
print("Number of Estimators:", etr.n_estimators)
print("Number of Features:", etr.n_features_)
print("Number of Outputs:", etr.n_outputs_)
