# Import necessary libraries
from sklearn.linear_model import BayesianRidge
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit the Bayesian ARD regression model
ard_model = BayesianRidge(tol=1e-8, n_iter=500, verbose=True)
ard_model.fit(X_train, y_train)

# Print the estimated models parameters and precisions
print("Weights:", ard_model.coef_)
print("Bias:", ard_model.intercept_)
print("Precisions (lambda):", ard_model.lambda_)
print("Precision of noise (alpha):", ard_model.alpha_)

# Plot the data and the predicted values
plt.scatter(y_train, ard_model.predict(X_train))
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.show()
