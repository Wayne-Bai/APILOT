from sklearn.linear_model import BayesianRidge
import numpy as np

# Example Data
# X: feature matrix, y: target vector
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])

# Create and train the Bayesian Ridge Regression model
model = BayesianRidge()
model.fit(X, y)

# Now model is ready to predict from feature inputs
predictions = model.predict(X)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", predictions)
