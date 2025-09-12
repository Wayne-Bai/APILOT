from sklearn.metrics import explained_variance_score
import numpy as np

# Creating some sample data
# True values
y_true = np.array([3, -0.5, 2, 7])
# Predicted values
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculating Explained Variance Score
evs = explained_variance_score(y_true, y_pred)

print(f"Explained Variance Score: {evs}")
