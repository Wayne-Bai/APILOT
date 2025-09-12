import numpy as np
from sklearn.metrics import explained_variance_score

# Example data
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate the explained variance score
score = explained_variance_score(y_true, y_pred)

print(f"Explained Variance Score: {score}")
