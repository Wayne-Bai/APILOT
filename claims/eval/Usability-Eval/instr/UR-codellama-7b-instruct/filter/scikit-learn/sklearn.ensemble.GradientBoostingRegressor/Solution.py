import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# Load the Boston housing dataset
boston = load_boston()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

# Initialize the GradientBoostingRegressor model with default parameters
model = GradientBoostingRegressor()

# Train the model on the training set
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the performance of the model using mean squared error
mse = np.mean((y_test - y_pred) ** 2)
print("Mean Squared Error: {:.2f}".format(mse))
