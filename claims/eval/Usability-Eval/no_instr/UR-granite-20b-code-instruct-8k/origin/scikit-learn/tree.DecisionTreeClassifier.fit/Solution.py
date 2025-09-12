from sklearn import tree

# Assuming X is the feature matrix and y is the target variable
# Create a decision tree classifier object
clf = tree.DecisionTreeClassifier()

# Train the decision tree classifier using the training set
clf = clf.fit(X, y)
