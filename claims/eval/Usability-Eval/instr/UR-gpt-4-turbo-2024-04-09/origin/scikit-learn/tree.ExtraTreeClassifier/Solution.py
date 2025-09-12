from sklearn.ensemble import ExtraTreesClassifier

# Create an Extremely Randomized Trees classifier
extremely_randomized_tree = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Sample data (features) and targets (labels)
X = [[0, 0], [1, 1], [1, 0], [0, 1]]  # Features
y = [0, 1, 1, 0]  # Labels

# Fit the model on the data
extremely_randomized_tree.fit(X, y)

# Making a prediction
prediction = extremely_randomized_tree.predict([[1, 0]])  # Predicting the label for input [1, 0]
print("Predicted label:", prediction)
