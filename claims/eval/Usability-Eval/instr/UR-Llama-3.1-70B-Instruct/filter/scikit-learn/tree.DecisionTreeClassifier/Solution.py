# Importing necessary libraries
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn import tree

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Create Decision Tree Classifier object
clf = DecisionTreeClassifier(random_state=1)

# Training the classifier using the training data
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Model Precision
print("Precision:", metrics.precision_score(y_test, y_pred, average='weighted'))

# Model Recall
print("Recall:", metrics.recall_score(y_test, y_pred, average='weighted'))
