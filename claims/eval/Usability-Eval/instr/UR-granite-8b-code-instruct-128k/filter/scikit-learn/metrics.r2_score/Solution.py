from sklearn.metrics import r2_score

# Assume you have already fitted your model and have predicted values stored in y_pred and actual values stored in y_true

# Calculate the R^2 score
r2_score = r2_score(y_true, y_pred)

print("R^2 score:", r2_score)
