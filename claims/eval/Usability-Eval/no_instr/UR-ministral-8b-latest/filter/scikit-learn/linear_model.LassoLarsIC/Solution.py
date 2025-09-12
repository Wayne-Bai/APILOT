from sklearn.linear_model import Lasso
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.linear_model import Lars

# Load dataset
boston = datasets.load_boston()

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=42)

# Define the Lasso regression model
lasso = Lasso(alpha=0.1)

# Fit the Lasso model
lasso.fit(X_train, y_train)

# Predict using the Lasso model
y_pred = lasso.predict(X_test)

# Compute the mean squared error
mse = mean_squared_error(y_test, y_pred)

print(f"Lasso Mean Squared Error: {mse}")

# Define the LARS model
from sklearn.linear_model import LassoLarsCV

# Fit the LARS model using BIC
lars_bic = LassoLarsCV(cv=10, penalty="filter").fit(X_train, y_train)
y_pred_bic = lars_bic.predict(X_test)

# Compute the mean squared error for the LARS model using BIC
mse_bic = mean_squared_error(y_test, y_pred_bic)

print(f"LARS Mean Squared Error using BIC: {mse_bic}")

# Define the LARS model
lars_aic = LassoLarsCV(cv=10, penalty="filter", selection_criteria='aic').fit(X_train, y_train)
y_pred_aic = lars_aic.predict(X_test)

# Compute the mean squared error for the LARS model using AIC
mse_aic = mean_squared_error(y_test, y_pred_aic)

print(f"LARS Mean Squared Error using AIC: {mse_aic}")
