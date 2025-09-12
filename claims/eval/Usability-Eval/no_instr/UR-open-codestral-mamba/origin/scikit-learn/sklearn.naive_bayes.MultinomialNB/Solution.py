from sklearn.naive_bayes import MultinomialNB

# Assuming we have X_train, y_train, X_test, y_test ready
# X_train and X_test are your feature vectors, y_train and y_test are your labels

# Create a Naive Bayes classifier
clf = MultinomialNB()

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Predict the test data
predictions = clf.predict(X_test)

# If you want to know the accuracy of the model
from sklearn.metrics import accuracy_score
print("Accuracy:", accuracy_score(y_test, predictions))
