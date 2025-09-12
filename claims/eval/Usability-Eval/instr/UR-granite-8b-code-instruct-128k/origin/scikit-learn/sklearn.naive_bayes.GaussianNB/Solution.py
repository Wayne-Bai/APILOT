from sklearn.naive_bayes import GaussianNB
import numpy as np

# Create a Gaussian Naive Bayes classifier
clf = GaussianNB()

# Train the classifier on a dataset
X = np.array([[0, 0], [1, 1]])
y = np.array([0, 1])
clf.fit(X, y)

# Make predictions on new data
predictions = clf.predict([[2, 2], [3, 3]])
print(predictions)
