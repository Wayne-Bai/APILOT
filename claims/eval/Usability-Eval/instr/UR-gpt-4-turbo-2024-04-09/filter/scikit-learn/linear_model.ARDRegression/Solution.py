from sklearn.linear_model import ARDRegression
import numpy as np

# Generating some sample data
np.random.seed(0)
n_samples, n_features = 100, 20
X = np.random.randn(n_samples, n_features)
lambda_ = 4.
w = np.zeros(n_features)
relevant_features = np.random.randint(0, n_features, 10)
for i in relevant_features:
    w[i] = np.random.randn()
noise = np.random.randn(n_samples)
y = np.dot(X, w) + lambda_ * noise

# Fitting ARD Regression
model = ARDRegression()
model.fit(X, y)

# Estimated coefficients
print("Estimated coefficients:", model.coef_)

# Estimated precision of the weights
print("Estimated precision of the weights (lambda):", model.lambda_)

# Estimated precision of the noise
print("Estimated precision of the noise (alpha):", model.alpha_)
