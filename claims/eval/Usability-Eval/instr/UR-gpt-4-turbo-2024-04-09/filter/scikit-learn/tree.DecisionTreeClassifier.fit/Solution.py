import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])  # features
y = np.array([0, 1, 0, 1])                     # labels

# Creating the decision tree classifier
clf = DecisionTreeClassifier()

# Fitting the model
clf.fit(X, y)
