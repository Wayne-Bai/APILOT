import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 6, 10, 15])

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate R^2 score
r2 = r2_score(y, y_pred)
print(f'R^2 score: {r2}')
