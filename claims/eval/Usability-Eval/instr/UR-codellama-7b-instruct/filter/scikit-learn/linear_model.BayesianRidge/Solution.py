
from sklearn.linear_model import BayesianRidge
from skotlin.optimization import LBFGS
import numpy as np

# Generate some sample data
n_samples = 100
X = np.random.rand(n_samples, 2)
y = np.sin(X[:, 0] * (2 * np.pi)) + 0.5 * X[:, 1] ** 3 + np.random.normal(size=n_samples)

# Initialize the model and optimize the parameters
model = BayesianRidge()
optimizer = LBFGS(model.parameters())
optimizer.minimize(X, y)

# Print the optimized parameters
print("Lambda:", model.lambda_)
print("Alpha:", model.alpha)
