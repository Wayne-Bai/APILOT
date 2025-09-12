from sklearn.ensemble import ExtraTreesClassifier

# Initialize the classifier
clf = ExtraTreesClassifier(random_state=0)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
