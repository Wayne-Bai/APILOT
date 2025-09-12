from sklearn.covariance import GraphicalLasso

# Assuming X is your data matrix
# X = ...

# Initialize the GraphicalLasso estimator with l1 penalty
graph_lasso = GraphicalLasso(alpha=0.1)

# Fit the estimator to the data
graph_lasso.fit(X)

# Get the estimated inverse covariance matrix
inverse_covariance = graph_lasso.get_covariance()

# Print the estimated inverse covariance matrix
print(inverse_covariance)
