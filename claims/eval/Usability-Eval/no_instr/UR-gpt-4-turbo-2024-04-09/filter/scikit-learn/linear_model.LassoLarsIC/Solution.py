import numpy as np
from sklearn.linear_model import LassoLarsIC

# Simulate some data
np.random.seed(42)
X = np.random.randn(100, 10)  # 100 samples with 10 features each
y = np.dot(X, np.array([1.5, -2.0, 0.0, 0.0, 3.5, 0.0, -1.0, 0.0, 0.0, 0.0])) + 0.5 * np.random.randn(100)

# Fit the LassoLarsIC model using the BIC criterion
model_bic = LassoLarsIC(criterion='bic', normalize=True)
model_bic.fit(X, y)

# Display the coefficients from the model
print("Coefficients using the BIC criterion:", model_bic.coef_)

# Optionally, fit using the AIC criterion
model_aic = LassoLarsIC(criterion='aic', normalize=True)
model_aic.fit(X, y)

# Display the coefficients from the model
print("Coefficients using the AIC criterion:", model_aic.coef_)
