# Import necessary libraries
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Boston house-prices dataset
boston_dataset = load_boston()

# Print the description and the feature names of the dataset
print("Dataset Description:\n", boston_dataset.DESCR)
print("Feature Names:\n", boston_dataset.feature_names)

# Split the dataset into features (X) and target variable (y)
X = boston_dataset.data
y = boston_dataset.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model using the training sets
model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
