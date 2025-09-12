from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import numpy as np

# Generate some data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 + 3*X + np.random.rand(100, 1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the explain variance score
explained_variance_score = r2_score(y_test, y_pred)

print(f"Explained Variance Score: {explained_variance_score}")
