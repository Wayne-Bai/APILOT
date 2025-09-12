from sklearn.covariance import GraphLassoCV

# Assuming X is your data matrix
model = GraphLassoCV()
model.fit(X)

# The optimal inverse covariance matrix is:
inverse_covariance = model.precision_

# The estimated model is available as:
model_ = model.covariance_
