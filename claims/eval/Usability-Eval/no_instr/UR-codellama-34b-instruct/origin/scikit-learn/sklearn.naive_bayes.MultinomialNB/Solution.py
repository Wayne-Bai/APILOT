
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import numpy as np

# Generate some dummy data
X = np.random.rand(100, 10)
y = np.random.randint(0, 2, size=100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Use the trained model to predict the labels for the testing data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier on the testing data
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)
