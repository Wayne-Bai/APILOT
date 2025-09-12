from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Assuming X and y are your input data and target variable respectively
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Specify the number of components
n_components = 2

# Create the Partial Least Squares SVD object
pls = PLSRegression(n_components)

# Fit the model to the data
pls.fit(X, y)

# Make predictions
predictions = pls.predict(X)
