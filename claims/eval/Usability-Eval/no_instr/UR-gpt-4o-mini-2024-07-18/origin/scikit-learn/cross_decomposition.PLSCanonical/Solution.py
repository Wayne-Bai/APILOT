from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Example dataset
X = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.9],
              [1.0, 1.1, 1.2]])
y = np.array([1, 2, 3, 4])

# Create the PLS Regression model
pls = PLSRegression(n_components=2)

# Fit the model
pls.fit(X, y)

# Transform the data
X_transformed = pls.transform(X)

# Make predictions
y_pred = pls.predict(X)

print("Transformed X:\n", X_transformed)
print("Predicted y:\n", y_pred)
