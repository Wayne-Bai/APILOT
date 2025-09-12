import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Generate a dummy dataset
X, y = make_regression(n_samples=100, n_features=20, noise=0.1, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Lasso model
lasso = Lasso()

# Fit the model using Lasso
lasso.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lasso.predict(X_test)

# Calculate the mean squared error on the test set
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Calculate the BIC and AIC for model selection
n = X.shape[1]
m = X.shape[0] - 1
bic = len(lasso.coef_) * np.log(mse / 2)
aic = 2 * n * np.log(mse / 2)

print('BIC:', bic)
print('AIC:', aic)
