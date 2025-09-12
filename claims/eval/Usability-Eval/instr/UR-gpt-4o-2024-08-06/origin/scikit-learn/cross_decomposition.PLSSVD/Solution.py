import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import PLSCanonical
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Create a dataset
X, Y = make_regression(n_samples=100, n_features=10, n_informative=10, noise=0.1, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize the PLSCanonical model
pls_canonical = PLSCanonical(n_components=2)

# Fit the model to the training data
pls_canonical.fit(X_train, Y_train)

# Transform both the training and test sets
X_train_transformed, Y_train_transformed = pls_canonical.transform(X_train, Y_train)
X_test_transformed, Y_test_transformed = pls_canonical.transform(X_test, Y_test)

# Predict using the model
Y_pred = pls_canonical.predict(X_test)

# Compute and print the Mean Squared Error
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)
