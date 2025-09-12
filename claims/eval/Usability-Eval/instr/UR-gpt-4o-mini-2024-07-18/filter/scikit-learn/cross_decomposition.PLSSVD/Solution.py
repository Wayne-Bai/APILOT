from sklearn.cross_decomposition import PLSRegression
import numpy as np

# Example data
X = np.random.rand(10, 5)  # Predictor matrix with 10 samples and 5 features
Y = np.random.rand(10, 2)   # Response matrix with 10 samples and 2 targets

# Create a PLSRegression model
pls = PLSRegression(n_components=2)

# Fit the model to the data
pls.fit(X, Y)

# Transform the predictors to the PLS space
X_p = pls.transform(X)

# Fit the regression model (in PLS space)
Y_pred = pls.fit_transform(X, Y)

# Output the transformed predictors and predicted responses
print("Transformed predictors:\n", X_p)
print("Predicted responses:\n", Y_pred)
