# Import necessary libraries
from sklearn.cross_decomposition import PLSCanonical, PLSRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate some data for demonstration
np.random.seed(0)
n_samples = 400
n_features = 10
X = np.random.normal(size=(n_samples, n_features))
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.normal(size=n_samples)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Partial Least Square SVD (PLS) regression object
pls = PLSRegression(n_components=2)

# Train the model using the training data
pls.fit(X_train, y_train)

# Make predictions using the test data
y_pred = pls.predict(X_test)

# Calculate the mean squared error of the predictions
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.2f}")

# Create a PLS canonical object (alternative to PLSRegression for a different output)
plscanonical = PLSCanonical(n_components=2)

# Train the model using the training data
plscanonical.fit(X_train, y_train)

# Transform the data into the new coordinate system
X_trans = plscanonical.transform(X_train, y_train)

# Transform the data back to the original coordinate system
X_back = plscanonical.inverse_transform(X_trans)
