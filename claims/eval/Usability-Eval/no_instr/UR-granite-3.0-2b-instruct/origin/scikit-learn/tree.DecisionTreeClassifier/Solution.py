from sklearn.tree import DecisionTreeClassifier

# Assuming X is the features and y is the target variable
# DecisionTreeClassifier() creates a decision tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier with the training data
clf.fit(X, y)

# Make predictions using the trained classifier
predictions = clf.predict(X)
