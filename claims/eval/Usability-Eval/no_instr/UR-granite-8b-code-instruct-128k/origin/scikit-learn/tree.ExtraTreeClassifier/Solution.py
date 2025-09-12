from sklearn.ensemble import RandomForestClassifier

# create a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# fit the classifier to the training data
clf.fit(X_train, y_train)

# make predictions on the test data
predictions = clf.predict(X_test)

# evaluate the accuracy of the classifier
accuracy = clf.score(X_test, y_test)

print("Accuracy:", accuracy)
