from sklearn.naive_bayes import ComplementNB

# Create a Complement Naive Bayes classifier object
classifier = ComplementNB()

# Train the classifier using the training data
classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = classifier.predict(X_test)
