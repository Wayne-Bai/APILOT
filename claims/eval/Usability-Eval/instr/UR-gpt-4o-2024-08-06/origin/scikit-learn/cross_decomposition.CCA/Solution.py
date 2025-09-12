import numpy as np
from sklearn.cross_decomposition import PLSRegression

# Create some example data
np.random.seed(0)
X = np.random.normal(size=(100, 10))  # 100 samples, 10 features
Y = np.random.normal(size=(100, 3))   # 100 samples, 3 dimensions

# Initialize PLS Regression for Canonical Correlation Analysis
n_components = min(X.shape[1], Y.shape[1])  # Typically min(number of X features, number of Y features)
pls = PLSRegression(n_components=n_components)

# Fit the model
pls.fit(X, Y)

# Transform both sets of variables
X_c, Y_c = pls.transform(X, Y)

# Results: 
# X_c and Y_c are the scores in the canonical space
# The model can be used further for analysis or prediction

print("X_c (Canonical scores of X):\n", X_c)
print("Y_c (Canonical scores of Y):\n", Y_c)
