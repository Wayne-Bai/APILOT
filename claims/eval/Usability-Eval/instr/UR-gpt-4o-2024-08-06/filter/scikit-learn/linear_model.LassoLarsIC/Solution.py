import numpy as np
from sklearn.linear_model import LassoLars
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate a sample dataset
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize BIC/AIC selection values
criterion_score = {'AIC': float('inf'), 'BIC': float('inf')}
best_model = None

# Looping over possible models with different alpha values
alphas = np.linspace(0.01, 1.0, 100)
for alpha in alphas:
    # Fit the LassoLars model
    model = LassoLars(alpha=alpha, max_iter=1000)
    model.fit(X_train, y_train)

    # Calculate the log-likelihood and number of parameters (non-zero coefficients)
    predictions = model.predict(X_train)
    residual = y_train - predictions
    sse = np.sum(residual ** 2)
    sigma2 = sse / len(y_train)
    log_likelihood = -0.5 * len(y_train) * (np.log(2 * np.pi * sigma2) + 1)

    # Number of non-zero coefficients (complexity penalty)
    num_params = np.sum(model.coef_ != 0)

    # Calculate AIC and BIC
    AIC = -2 * log_likelihood + 2 * num_params
    BIC = -2 * log_likelihood + num_params * np.log(len(y_train))

    # Update the best model if this one has the lowest AIC or BIC
    if AIC < criterion_score['AIC']:
        criterion_score['AIC'] = AIC
        best_model_AIC = model

    if BIC < criterion_score['BIC']:
        criterion_score['BIC'] = BIC
        best_model_BIC = model

# Make predictions with the best model according to AIC
y_pred_aic = best_model_AIC.predict(X_test)
mse_aic = mean_squared_error(y_test, y_pred_aic)
print("Best model according to AIC - Mean Squared Error on test set:", mse_aic)

# Make predictions with the best model according to BIC
y_pred_bic = best_model_BIC.predict(X_test)
mse_bic = mean_squared_error(y_test, y_pred_bic)
print("Best model according to BIC - Mean Squared Error on test set:", mse_bic)
