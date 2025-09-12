from sklearn.linear_model import BayesianRidge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the Bayesian Ridge Regression model
model = BayesianRidge()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Optionally, you can print the coefficients and the intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
