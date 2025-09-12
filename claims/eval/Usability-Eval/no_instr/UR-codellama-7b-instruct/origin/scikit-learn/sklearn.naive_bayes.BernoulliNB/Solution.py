from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import make_classification

# Generate a synthetic dataset
X, y = make_classification(n_samples=100, n_classes=5, random_state=42)

# Create a naive Bayes classifier
clf = MultinomialNB()

# Train the classifier on the data
clf.fit(X, y)

# Predict the output for a new set of input features
new_features = [[1, 2, 3, 4, 5]]
prediction = clf.predict(new_features)
print("Predicted class:", prediction)
