from sklearn.linear_model import RidgeCV
from sklearn.datasets import make_regression
from sklearn.model_selection import GridSearchCV

# Generate a synthetic dataset
X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)

# Create a RidgeCV object with a grid of alpha values
alphas = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]
ridge_cv = RidgeCV(alphas=alphas, cv=5)

# Fit the model
ridge_cv.fit(X, y)

# Print the best alpha value and the corresponding mean squared error
print(f"Best alpha: {ridge_cv.alpha_}")
print(f"Mean squared error: {ridge_cv.mean_squared_error_}")
