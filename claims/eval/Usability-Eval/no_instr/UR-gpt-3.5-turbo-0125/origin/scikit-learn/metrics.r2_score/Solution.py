
from sklearn.metrics import r2_score

# True y values
y_true = [3, -0.5, 2, 7]

# Predicted y values
y_pred = [2.5, 0.0, 2, 8]

# Calculating the coefficient of determination (R^2 score)
r2 = r2_score(y_true, y_pred)

print(f'R^2 Score: {r2}')
