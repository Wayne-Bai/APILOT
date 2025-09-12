# Import necessary libraries
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import BayesianRidge
import numpy as np
import matplotlib.pyplot as plt

# Generate a regression dataset
X, y = make_regression(n_samples=100, n_features=10, n_informative=6, noise=0.5)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the Bayesian Ridge model
br = BayesianRidge()
br.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = br.predict(X_test)

# Print the coefficients of the model
print("Coefficients:", br.coef_)

# Plot the predicted vs actual values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.show()

# Print the score (coefficient of determination) of the model
print("Score: ", br.score(X_test, y_test))
