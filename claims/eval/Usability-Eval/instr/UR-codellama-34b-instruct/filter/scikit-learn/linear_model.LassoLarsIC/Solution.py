import numpy as np
from sklearn.linear_model import Lars
from sklearn.metrics import bic, aic

# Generate some example data
n_samples = 100
n_features = 20
X = np.random.rand(n_samples, n_features)
y = np.random.rand(n_samples)

# Initialize the Lars model
lars = Lars()

# Fit the Lasso model with Lars using BIC for model selection
lars.fit(X, y, alpha=0.1, method='bic')
print("BIC:", bic(lars))

# Fit the Lasso model with Lars using AIC for model selection
lars.fit(X, y, alpha=0.1, method='aic')
print("AIC:", aic(lars))
