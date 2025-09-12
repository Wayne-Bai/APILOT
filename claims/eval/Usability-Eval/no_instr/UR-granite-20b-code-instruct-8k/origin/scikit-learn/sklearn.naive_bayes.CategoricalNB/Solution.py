from sklearn.naive_bayes import MultinomialNB

# Create an instance of the Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier using your training data and labels
clf.fit(X_train, y_train)

# Make predictions on new data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
