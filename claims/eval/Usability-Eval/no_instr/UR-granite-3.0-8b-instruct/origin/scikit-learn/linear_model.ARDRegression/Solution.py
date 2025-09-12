from sklearn.linear_model import BayesianRidge
import numpy as np

# Assuming X is the features and y is the target variable
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([1, 2, 3])

# Initialize the Bayesian Ridge Regression model
model = BayesianRidge(compute_score=True, fit_intercept=True, copy_X=True, t=1.0, alpha_1=1e-06, alpha_2=1e-06, lambda_1=1e-06, lambda_2=1e-06, alpha_3=1e-06, n_iter=300, tol=0.001, verbose=0)

# Fit the model
model.fit(X, y)

# Print the estimated parameters
print("Estimated weights: ", model.coef_)
print("Estimated precisions of the distributions of the weights: ", model.alpha_)
print("Estimated precision of the distribution of the noise: ", model.lambda_)
