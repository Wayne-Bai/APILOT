from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

# Train a random forest classifier on the dataset
clf = ExtraTreesClassifier()
clf.fit(X, y)

# Create a SelectFromModel instance with threshold=0.1
sfm = SelectFromModel(clf, threshold=0.1)

# Fit the selector on the training data
sfm.fit(X, y)

# Use the selector to transform the data
X_selected = sfm.transform(X)
