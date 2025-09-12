from sklearn.metrics import explained_variance_score
import numpy as np

# Sample true values and predicted values
y_true = np.array([3.0, -0.5, 2.0, 7.0])
y_pred = np.array([2.5, 0.0, 2.0, 8.0])

# Calculate explained variance score
ev_score = explained_variance_score(y_true, y_pred)

print("Explained Variance Score:", ev_score)
