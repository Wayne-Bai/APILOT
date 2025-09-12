from sklearn.covariance import GraphicalLassoCV
import numpy as np

# Assuming you have some data in a numpy array called X
X = np.array([[...]])

# Create a GraphicalLassoCV object
glasso_cv = GraphicalLassoCV()

# Fit data to the model
glasso_cv.fit(X)

# The sparse inverse covariance is now stored in glasso_cv.covariance_
# The l1 penalty chosen by cross-validation is stored in glasso_cv.alpha_
