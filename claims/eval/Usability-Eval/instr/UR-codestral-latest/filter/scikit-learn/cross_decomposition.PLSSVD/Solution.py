from sklearn.cross_decomposition import PLSRegression
import numpy as np

# A hypothetical X and Y array for data
# Replace X and Y with your actual data
X = np.random.rand(100, 5)
Y = np.random.rand(100, 1)

# Create PLSRegression object
pls = PLSRegression(n_components=2)

# Fit PLS model
pls.fit(X, Y)

# Print out the coeffcients of each predictor variable
print(pls.coef_)

