from sklearn.tree import DecisionTreeClassifier

# Sample training data
X = [[0, 0], [1, 1]]
y = [0, 1]

# Create Decision Tree classifier
clf = DecisionTreeClassifier()

# Fitting the model with the training data
clf.fit(X, y)
