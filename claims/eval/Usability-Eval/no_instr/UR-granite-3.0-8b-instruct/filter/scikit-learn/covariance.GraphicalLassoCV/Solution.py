from sklearn.covariance import GraphicalLassoCV
import numpy as np

# Assume X is your data matrix
X = np.random.randn(100, 5)

# Initialize the GraphicalLassoCV estimator
graphic_lasso = GraphicalLassoCV(cv=5, random_state=0)

# Fit the estimator to the data
graphic_lasso.fit(X)

# Print the estimated precision matrix
print(graphic_lasso.precision_)
