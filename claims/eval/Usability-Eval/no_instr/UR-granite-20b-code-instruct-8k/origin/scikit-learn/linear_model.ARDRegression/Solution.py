from sklearn.linear_model import BayesianRidge

# Assuming X is your input data and y are the targets
# And n_iter is the number of iterations for the EM algorithm
model = BayesianRidge(n_iter=n_iter)
model.fit(X, y)

# Get the estimated precision of the weights
lambda_values = model.lambda_

# Get the estimated precision of the noise
alpha_value = model.alpha_
