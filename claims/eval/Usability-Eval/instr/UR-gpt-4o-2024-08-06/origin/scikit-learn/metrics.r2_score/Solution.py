import numpy as np
from sklearn.metrics import r2_score

# Example true values and predicted values
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

# Compute the R^2 score
r2 = r2_score(y_true, y_pred)

# Output the score
print("Coefficient of determination (R^2):", r2)
