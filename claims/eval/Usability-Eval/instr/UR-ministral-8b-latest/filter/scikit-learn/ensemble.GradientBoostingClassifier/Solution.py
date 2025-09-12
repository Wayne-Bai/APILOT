import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

# Sample data for demonstration (replace with your own data)
X_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([0, 1, 0])

# Initialize the GradientBoostingClassifier
gbc = GradientBoostingClassifier()

# Fit the model
gbc.fit(X_train, y_train)

# Make predictions
X_test = np.array([[3, 5], [4, 6]])
predictions = gbc.predict(X_test)

print("Predictions:", predictions)
