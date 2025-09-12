from sklearn.linear_model import LassoLars
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming X is your feature matrix and y is your target variable
X = ...  # your feature matrix
y = ...  # your target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the LassoLars model
lasso_lars = LassoLars()

# Fit the model and get the best alpha using BIC
alphas = np.logspace(-4, -0.5, 300)
best_alpha = None
best_bic = float('inf')

for alpha in alphas:
    lasso_lars.alpha = alpha
    lasso_lars.fit(X_train, y_train)
    y_pred = lasso_lars.predict(X_test)
    bic = mean_squared_error(y_test, y_pred, squared=False) + np.log(len(y)) * lasso_lars.n_features_
    if bic < best_bic:
        best_alpha = alpha
        best_bic = bic

# Fit the final model with the best alpha
lasso_lars.alpha = best_alpha
lasso_lars.fit(X_train, y_train)

# Print the best alpha and the final model coefficients
print(f"Best alpha: {best_alpha}")
print(f"Final model coefficients: {lasso_lars.coef_}")
