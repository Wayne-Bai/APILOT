from sklearn.metrics import r2_score

# Example usage
# True values
y_true = [3, -0.5, 2, 7]

# Predictions from a regression model
y_pred = [2.5, 0.0, 2, 8]

# Calculate the coefficient of determination (R^2 score)
r2 = r2_score(y_true, y_pred)

print(f"Coefficient of determination (R^2 score): {r2}")
