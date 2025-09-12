from sklearn.metrics import explained_variance_score

# Example usage:
# y_true: True target values
# y_pred: Predicted target values

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

explained_variance = explained_variance_score(y_true, y_pred)
print("Explained Variance Score:", explained_variance)
