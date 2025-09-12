
from sklearn.linear_model import LassoLars
from sklearn.model_selection import train_test_split
import numpy as np

# Generate some random data for demonstration
np.random.seed(42)
X = np.random.rand(100, 10)
y = np.random.rand(100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit Lasso model with Lars using BIC for model selection
alpha = 1.0  # Regularization strength
lassolars = LassoLars(criterion='bic', alpha=alpha)
lassolars.fit(X_train, y_train)
print("Model coefficients:", lassolars.coef_)
