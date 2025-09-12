from sklearn.metrics import r2_score
y_true = ... # Replace with true y values
y_pred = ... # Replace with predicted y values
score = r2_score(y_true, y_pred)
print("Coefficient of determination (R^2) score:", score)
