import numpy as np
from sklearn.linear_model import LassoLarsIC
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the sample diabetes dataset
data = load_diabetes()
X = data.data
y = data.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the LassoLarsIC model with BIC (Bayesian Information Criterion)
# or AIC (Akaike Information Criterion) for model selection
model_bic = LassoLarsIC(criterion='bic')
model_aic = LassoLarsIC(criterion='aic')

# Fit the models to the training data
model_bic.fit(X_train, y_train)
model_aic.fit(X_train, y_train)

# Get the models' coefficients, including the intercept
coeff_bic = model_bic.coef_
intercept_bic = model_bic.intercept_

coeff_aic = model_aic.coef_
intercept_aic = model_aic.intercept_

# Make predictions on the testing data using both models
y_pred_bic = model_bic.predict(X_test)
y_pred_aic = model_aic.predict(X_test)

# Evaluate the performance of both models using Mean Squared Error
mse_bic = mean_squared_error(y_test, y_pred_bic)
mse_aic = mean_squared_error(y_test, y_pred_aic)

print(f"Mean Squared Error (BIC): {mse_bic}")
print(f"Mean Squared Error (AIC): {mse_aic}")
