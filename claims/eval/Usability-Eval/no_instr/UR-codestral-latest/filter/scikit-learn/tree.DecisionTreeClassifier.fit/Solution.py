from sklearn.tree import DecisionTreeClassifier

# Assuming X and y are your training data and target variables
clf = DecisionTreeClassifier(random_state=0)
clf = clf.fit(X, y)
