import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 4, 2, 5, 7])

# Create the model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Predict using the model
y_pred = model.predict(X)

# Calculate the R2 score
r2 = r2_score(y, y_pred)
