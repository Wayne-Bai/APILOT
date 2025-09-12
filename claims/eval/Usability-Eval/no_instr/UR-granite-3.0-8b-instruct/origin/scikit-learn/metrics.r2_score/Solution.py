from sklearn.metrics import r2_score

# Assuming y_true and y_pred are your true and predicted values respectively
y_true = [...]
y_pred = [...]

# Calculate the R^2 score
r2 = r2_score(y_true, y_pred)

print(f'R^2 score: {r2}')
