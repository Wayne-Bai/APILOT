import numpy as np
from sklearn.cross_decomposition import PLSRegression

# Example usage of PLSRegression (PLS1 which is a variant of PLS)
# Assuming X is the input features and y is the target variable
# n_components can be set to the desired number of components

X = np.random.rand(100, 2)  # Example input features
y = np.random.rand(100)     # Example target variable

# Create the PLSRegression object
pls = PLSRegression(n_components=1, store_covariance=True)  # Setting n_components=1 for PLS1

# Fit the model
pls.fit(X, y)

# Prediction
y_pred = pls.predict(X)
print("Predicted values:", y_pred)
