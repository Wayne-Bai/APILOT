from sklearn.naive_bayes import BernoulliNB

# Example data: binary matrix X and labels y
X = [[0, 1, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0]]
y = [1, 0, 1, 0]

# Training the model
model = BernoulliNB()
model.fit(X, y)

# Predicting the labels
predictions = model.predict(X)
print("Predictions:", predictions)

# Evaluating the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y, predictions)
print("Accuracy:", accuracy)
