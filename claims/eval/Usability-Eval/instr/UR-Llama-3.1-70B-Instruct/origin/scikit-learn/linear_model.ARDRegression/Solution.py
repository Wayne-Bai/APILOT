# Import necessary libraries
import numpy as np
from sklearn.linear_model import ARDRegression
import matplotlib.pyplot as plt

# Sample data
np.random.seed(0)
n_samples, n_features = 100, 100
X = np.random.randn(n_samples, n_features)

# Decreasing coef w. alternated signs for visualization
idx = np.arange(n_features)
coef = (-1) ** idx * np.exp(-idx / 10)
y = np.dot(X, coef)

# Add noise
y += 0.2 * np.random.normal(size=n_samples)

# Fit the model
ard = ARDRegression()
ard.fit(X, y)

# Print the estimated parameters
print("Estimated lambda (weights precisions):", ard.lambda_)
print("Estimated alpha (noise precision):", ard(alpha=1e-4))

# Plot the weights
plt.plot(coef, 'b', label="Ground truth")
plt.plot(ard.coef_, 'r', label="ARD estimate")
plt.legend()
plt.show()
