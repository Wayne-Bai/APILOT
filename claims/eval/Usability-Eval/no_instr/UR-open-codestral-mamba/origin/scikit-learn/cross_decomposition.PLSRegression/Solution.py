from sklearn.cross_decomposition import PLSRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes = load_diabetes()

# Use only one feature for simplicity
X = diabetes.data[:, 2:3]
y = diabetes.target

# Split the data into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create PLS regression object
pls = PLSRegression(n_components=2)

# Train the model using the training sets
pls.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = pls.predict(X_test)

# The mean squared error
mse = mean_squared_error(y_test, y_pred)

print(f"Mean squared error: {mse}")
