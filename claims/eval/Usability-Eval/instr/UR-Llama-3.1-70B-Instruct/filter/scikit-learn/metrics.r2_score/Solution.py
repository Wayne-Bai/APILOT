# Import necessary libraries
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate random data for demonstration
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X + 2 + np.random.randn(100, 1) / 1.5

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the R2 score
r2 = r2_score(y_test, y_pred)

print("Coefficient of determination (R2 score):", r2)

# Predict the average y and calculate the R2 score
average_y = np.mean(y_train) * np.ones_like(y_test)
average_r2 = r2_score(y_test, average_y)

print("R2 score for constant model (always predicts average y):", average_r2)

# Plot the data and the predictions
plt.scatter(X_test, y_test, label='Actual')
plt.scatter(X_test, y_pred, label='Predicted')
plt.scatter(X_test, average_y, label='Average y')
plt.legend()
plt.show()
