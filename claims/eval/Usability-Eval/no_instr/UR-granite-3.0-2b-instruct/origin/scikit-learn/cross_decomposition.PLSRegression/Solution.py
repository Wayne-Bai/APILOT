from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate a random regression dataset
X, y = make_regression(n_samples=100, n_features=20, n_targets=2, noise=0.1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the PLS regression model
pls = PLSRegression(n_components=2)

# Fit the model to the training data
pls.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = pls.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print(f"Mean Squared Error: {mse}")
