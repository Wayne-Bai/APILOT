import numpy as np
from sklearn.linear_model import LassoLarsCV
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.datasets import make_regression

# Generate some data
X, y = make_regression(n_samples=100, n_features=20, noise=0.1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# LassoLarsCV with BIC or AIC for model selection
model = LassoLarsCV(cv=5, precompute='arithmetic_mean', max_iter=1000, verbose=True)

# Fit the model
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# Calculate the score using MSE
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Get BIC and AIC values from the model
bic = model.bic_
aic = model.aic_
print(f"BIC: {bic}")
print(f"AIC: {aic}")
