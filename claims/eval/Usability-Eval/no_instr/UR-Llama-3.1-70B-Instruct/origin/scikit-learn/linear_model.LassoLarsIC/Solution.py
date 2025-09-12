# Import necessary libraries from scikit-learn
from sklearn.linear_model import LassoLarsIC
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import numpy as np

# Generate a random regression dataset
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Lasso model with Lars using BIC for model selection
lasso_bic = LassoLarsIC(criterion='bic', random_state=42)

# Fit the Lasso model with Lars using BIC
lasso_bic.fit(X_train, y_train)

# Create a Lasso model with Lars using AIC for model selection
lasso_aic = LassoLarsIC(criterion='aic', random_state=42)

# Fit the Lasso model with Lars using AIC
lasso_aic.fit(X_train, y_train)

# Get the coefficients of the Lasso model with Lars using BIC and AIC
print('Coefficients (BIC):', lasso_bic.coef_)
print('Coefficients (AIC):', lasso_aic.coef_)

# Predict using the Lasso model with Lars using BIC and AIC
y_pred_bic = lasso_bic.predict(X_test)
y_pred_aic = lasso_aic.predict(X_test)

# Evaluate the Lasso model with Lars using BIC and AIC
print('Score (BIC):', lasso_bic.score(X_test, y_test))
print('Score (AIC):', lasso_aic.score(X_test, y_test))
