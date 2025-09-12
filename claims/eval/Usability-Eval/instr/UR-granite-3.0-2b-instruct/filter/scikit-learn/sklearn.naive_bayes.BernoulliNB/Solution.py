from sklearn.naive_bayes import MultinomialNB

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)
