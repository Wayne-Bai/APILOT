import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate some sample data
np.random.seed(0)
n_samples = 100
X = np.random.rand(n_samples, 5)
y = np.random.rand(n_samples)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a PLS regression object and fit it to the training data
pls = PLSRegression(n_components=5)
pls.fit(X_train, y_train)

# Use the fitted model to predict the targets for the testing set
y_pred = pls.predict(X_test)

# Evaluate the performance of the model using mean squared error and R2 score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean squared error: {mse:.4f}")
print(f"R2 score: {r2:.4f}")
