from sklearn.covariance import GraphicalLassoCV

# Sample data for illustrating the usage
X = [[0.23, 0.37], [0.85, 0.07], [0.58, 0.52], [1.08, -0.65], [0.37, -1.13], [0.11, -0.42], [0.13, -0.13], [0.89, -1.14], [0.57, -0.85], [1.03, -1.34]]

# Create GraphicalLassoCV object
graphical_lasso_cv = GraphicalLassoCV()

# Fit the model to the data
graphical_lasso_cv.fit(X)

# The object now contains the sparse inverse covariance in graphical_lasso_cv.precision_
