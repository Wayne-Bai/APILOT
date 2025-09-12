from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Example data (make sure your X and Y have the same number of rows (samples))
X = np.array([[0., 0., 1.], [1., 0., 0.], [0., 1., 1.], [1., 1., 0.]])
Y = np.array([[0.1], [0.9], [0.6], [1.2]])

# Create a Partial Least Squares model with specified number of components
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X, Y)

# Perform transformation
X_transformed = pls.transform(X)

# Predict the Y values
Y_pred = pls.predict(X)

print("Transformed X:\n", X_transformed)
print("Predicted Y:\n", Y_pred)
