from sklearn.metrics import explained_variance_score

# Sample data
y_true = [3, 0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate explained variance score
variance_score = explained_variance_score(y_true, y_pred)
print("Explained Variance Score:", variance_score)
