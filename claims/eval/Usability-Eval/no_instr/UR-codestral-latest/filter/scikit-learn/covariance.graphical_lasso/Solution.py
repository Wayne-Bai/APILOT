from sklearn.covariance import GraphLassoCV

# Sample data
X = [[0., 2., 2.], [2., 0., 2.], [2., 2., 2.]]

# Fit GraphLassoCV estimator
model = GraphLassoCV()
model.fit(X)

# Get the estimated precision matrix
precision_matrix = model.precision_
print(precision_matrix)
