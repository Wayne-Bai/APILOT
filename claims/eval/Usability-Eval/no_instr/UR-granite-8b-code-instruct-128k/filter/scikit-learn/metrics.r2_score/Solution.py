
from sklearn.metrics import r2_score

# Generate some example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Compute the R^2 score
r2_score(y_true, y_pred)
