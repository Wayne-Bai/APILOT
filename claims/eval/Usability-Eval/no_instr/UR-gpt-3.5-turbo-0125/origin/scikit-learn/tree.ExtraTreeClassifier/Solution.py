
from sklearn.ensemble import ExtraTreesClassifier

# Create an extremely randomized tree classifier
clf = ExtraTreesClassifier()

# Training the classifier
clf.fit(X_train, y_train)

# Making predictions
predictions = clf.predict(X_test)
