from sklearn.metrics import r2_score

# Assuming y_true and y_pred are your actual and predicted values respectively
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate the coefficient of determination
r2 = r2_score(y_true, y_pred)

print(f'Coefficient of Determination (R^2 score): {r2}')
