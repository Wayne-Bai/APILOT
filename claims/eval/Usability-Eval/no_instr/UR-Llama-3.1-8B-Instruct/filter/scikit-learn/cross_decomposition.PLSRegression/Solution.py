# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Create sample data
np.random.seed(0)
X = np.random.rand(100, 10)  # Features
y = np.random.rand(100, 1)   # Target variable

# Define the PLS regression object
pls = PLSRegression(n_components=2)  # Number of principal components

# Fit the model
pls.fit(X, y)

# Print the coefficients (loadings and coefficients for X and y)
print("PLS Loadings for X:")
print(pls.x_scores_.shape)
print(pls.x_rotation_.shape)
print(pls.y_scores_.shape)

print("\nPLS Coefficients for Y:")
print(pls.y_loadings_.shape)

# Print the predicted values
y_pred = pls.predict(X)
print("\nPredicted Target Variable:")
print(y_pred.shape)

# Evaluate the model
print("\nModel Score:")
print(pls.score(X, y))

# Get the predicted values and residuals
y_pred, y_resid = pls.predict_and_transform(X), pls.transform(X) - pls.y_loadings_.dot(pls.x_scores_)
