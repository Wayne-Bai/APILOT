from sklearn.tree import DecisionTreeClassifier

# Create a decision tree classifier object
clf = DecisionTreeClassifier()

# Train the classifier using the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)
