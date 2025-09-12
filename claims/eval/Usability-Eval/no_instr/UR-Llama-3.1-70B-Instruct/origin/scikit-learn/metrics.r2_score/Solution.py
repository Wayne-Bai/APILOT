# Import necessary libraries
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Create a dataset
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Compute the R-squared score (coefficient of determination)
score = r2_score(y_test, y_pred)

print(f"R-squared score (coefficient of determination): {score:.2f}")

# Compare the R-squared score with a constant model
constant_y_pred = np.full_like(y_test, np.mean(y_train))
constant_score = r2_score(y_test, constant_y_pred)

print(f"R-squared score for a constant model: {constant_score:.2f}")
