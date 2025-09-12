from sklearn.naive_bayes import ComplementNB

# Create a Complement Naive Bayes classifier
clf = ComplementNB()

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)
