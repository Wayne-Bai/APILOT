from sklearn.naive_bayes import MultinomialNB

# Initialize the MultinomialNB classifier
clf = MultinomialNB()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Predict the labels of the test data
y_pred = clf.predict(X_test)
