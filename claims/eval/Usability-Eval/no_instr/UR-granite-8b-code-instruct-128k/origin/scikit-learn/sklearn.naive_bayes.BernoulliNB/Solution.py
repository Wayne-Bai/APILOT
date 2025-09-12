from sklearn.naive_bayes import BernoulliNB

# create an instance of the BernoulliNB classifier
clf = BernoulliNB()

# fit the classifier to the training data
clf.fit(X_train, y_train)

# make predictions on the test data
y_pred = clf.predict(X_test)

# evaluate the accuracy of the classifier
accuracy = clf.score(X_test, y_test)
