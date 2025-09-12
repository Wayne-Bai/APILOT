from sklearn.metrics import r2_score

# Assume y_true and y_pred are your true and predicted values respectively
score = r2_score(y_true, y_pred)

print("Coefficient of Determination (R^2 Score):", score)
