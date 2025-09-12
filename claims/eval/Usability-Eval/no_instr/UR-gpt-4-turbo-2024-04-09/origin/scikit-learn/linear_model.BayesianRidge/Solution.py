from sklearn.linear_model import BayesianRidge
import numpy as np

# Example data
# X: features (e.g., [[0, 0], [1, 1], [2, 2]])
# y: target values (e.g., [0, 1, 2])
X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

# Creating a Bayesian Ridge Regression model
model = BayesianRidge()

# Fit the model
model.fit(X, y)

# After fitting the model, you can inspect lambda (precision of the weights)
# and alpha (precision of the noise) which are optimized automatically
lambda_ = model.lambda_
alpha_ = model.alpha_

print("Lambda (precision of the weights):", lambda_)
print("Alpha (precision of the noise):", alpha_)

# You can also use the model to make predictions
predictions = model.predict([[1, 1]])
print("Predicted value:", predictions[0])
