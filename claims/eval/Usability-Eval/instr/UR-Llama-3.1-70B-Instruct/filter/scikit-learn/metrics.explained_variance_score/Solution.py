# Importing necessary libraries
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Generate random data for demonstration
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 + 2 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model = model.partial_fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the explained variance score
evs = explained_variance_score(y_test, y_pred)

print(f"Explained variance score: {evs:.2f}")
