from sklearn.metrics import r2_score

# Assuming y_true and y_pred are your true and predicted values
r2 = r2_score(y_true, y_pred)

print("Coefficient of Determination (R2 Score):", r2)
