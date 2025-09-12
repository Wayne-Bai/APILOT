from sklearn.linear_model import BayesianRidge

# Create an instance of the BayesianRidge class
reg = BayesianRidge()

# Fit the data (X is training data, y is target values)
reg.fit(X, y)

# Obtain the parameters: weights, lambda, alpha
weights = reg.coef_
lambda_ = 1 / reg.alpha_
alpha = 1 / reg.lambda_

print('Weights:', weights)
print('Lambda:', lambda_)
print('Alpha:', alpha)
