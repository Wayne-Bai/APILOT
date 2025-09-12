import numpy as np
from sklearn import linear_model

# Generate some synthetic data for demonstration:
# Number of samples
n_samples = 200
# Number of features
n_features = 100

np.random.seed(42)
X = np.random.randn(n_samples, n_features)
coef = 3 * np.random.randn(n_features)
inds = np.arange(n_features)
np.random.shuffle(inds)
coef[inds[10:]] = 0  # sparsify coef
y = np.dot(X, coef) + 0.01 * np.random.normal(size=n_samples)

# LassoLarsIC: Lasso model fit with the Lars algorithm using BIC or AIC for model selection
model_bic = linear_model.LassoLarsIC(criterion='bic')
model_aic = linear_model.LassoLarsIC(criterion='aic')

model_bic.fit(X, y)
model_aic.fit(X, y)

print("Estimated coefficients (BIC):", model_bic.coef_)
print("Estimated coefficients (AIC):", model_aic.coef_)
