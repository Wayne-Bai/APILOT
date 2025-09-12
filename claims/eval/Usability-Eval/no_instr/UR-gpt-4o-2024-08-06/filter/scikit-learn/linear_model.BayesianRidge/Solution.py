# Import necessary libraries from scikit-learn
from sklearn.linear_model import BayesianRidge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some regression data
X, y = make_regression(n_samples=100, n_features=20, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Bayesian Ridge Regression model
model = BayesianRidge()

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Display the mean squared error
print(f'Mean Squared Error: {mse:.4f}')

# Display optimized parameters
print("Lambda (precision of the weights):", model.lambda_)
print("Alpha (precision of the noise):", model.alpha_)
