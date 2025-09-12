from sklearn.linear_model import BayesianRegression
import numpy as np

# Assume our data is in X, y
X, y = np.random.randn(100, 3), np.random.randn(100)

# Apply Bayesian ARD regression
model = BayesianRegression(n_iter=500)
model.fit(X, y)

# Print the coefficients
print('Coefficients:', model.coef_)

# And the noise precision
print('Noise precision:', model.alpha_)
