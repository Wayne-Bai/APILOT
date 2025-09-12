
# Importing necessary libraries
import numpy as np
from sklearn.metrics import explained_variance_score

# Sample ground truth and predictions
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# Calculate explained variance regression score
explained_variance = explained_variance_score(y_true, y_pred)

print("Explained Variance Regression Score:", explained_variance)
