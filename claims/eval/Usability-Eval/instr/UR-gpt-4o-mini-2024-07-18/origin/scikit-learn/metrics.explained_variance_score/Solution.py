from sklearn.metrics import r2_score

# Example usage
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate the explained variance score using r2_score
explained_variance = r2_score(y_true, y_pred)

print("Explained Variance Score:", explained_variance)
