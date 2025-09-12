import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score

# Generate some sample data
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Get the y predictions
y_pred = model.predict(X)

# Calculate the explained variance score
score = explained_variance_score(y, y_pred)
print(f"Explained Variance Score: {score:.3f}")
