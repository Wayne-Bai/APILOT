from sklearn.metrics import r2_score

# Sample data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate the coefficient of determination (R^2 score)
r2 = r2_score(y_true, y_pred)

print("Coefficient of Determination, R^2 score:", r2)
