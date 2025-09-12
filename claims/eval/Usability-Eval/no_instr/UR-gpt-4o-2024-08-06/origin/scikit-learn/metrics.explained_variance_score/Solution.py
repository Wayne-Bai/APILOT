from sklearn.metrics import explained_variance_score

# Example: generating some sample data
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.0, 8.0]

# Calculating the explained variance score
explained_variance = explained_variance_score(y_true, y_pred)
print("Explained Variance Score:", explained_variance)
