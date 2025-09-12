
from sklearn.ensemble import ExtraTreesClassifier

# Create an extremely randomized tree classifier
clf = ExtraTreesClassifier()

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)
