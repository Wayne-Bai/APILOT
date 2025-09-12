from sklearn.neighbors import RadiusNeighborsClassifier

# Here, create an instance of the classifier
# assuming 'X' is data and 'y' is labels
clf = RadiusNeighborsClassifier(radius=1.0, outlier_label=-1)

# Fit the classifier
clf.fit(X, y)

# To predict, use the predict method
# assuming 'X_test' is the test data
predictions = clf.predict(X_test)
