from sklearn.linear_model import BayesianRidge
import numpy as np

# Generate some sample data
X = np.random.rand(100, 2)  # 100 samples, 2 features
y = X @ np.array([1.5, -2.0]) + np.random.randn(100) * 0.1  # Linear combination with noise

# Create and fit the Bayesian Ridge regression model
model = BayesianRidge()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Print model coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
