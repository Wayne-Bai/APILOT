import sklearn.tree as tree

# Assuming X and y are the input features and corresponding labels, respectively
X_train = ... # load your training dataset
y_train = ... # load your training labels

# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Now you can use clf.predict to make predictions on unseen data
