from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Sample data
X = np.array([[0.1, 0.2],
              [0.2, 0.4],
              [0.3, 0.6],
              [0.4, 0.8],
              [0.5, 1.0]])  # Feature matrix

Y = np.array([[1],
              [2],
              [3],
              [4],
              [5]])  # Target matrix

# Create a PLSRegression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X, Y)

# Predict using the model
Y_pred = pls.predict(X)

print("Predicted values:\n", Y_pred)
