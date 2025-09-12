import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Create a decision tree classifier object
clf = DecisionTreeClassifier()

# Example dataset
X = np.array([[2, 3], [4, 7], [1, 9], [11, 2], [12, 4], [14, 6], [3, 8]])
Y = np.array([0, 0, 0, 0, 1, 1, 1])

# Split the dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Train the decision tree classifier on the training sets
clf.fit(X_train, Y_train)

# Use the trained model to make predictions on the test set
Y_pred = clf.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = metrics.accuracy_score(Y_test, Y_pred)

# Print out the accuracy
print(f'Accuracy: {accuracy}')

# Plot the decision tree
plt.figure(figsize=(12,8))
from sklearn.tree import plot_tree
plot_tree(clf, feature_names=['Feature 1', 'Feature 2'], class_names=['Class 0', 'Class 1'], filled=True)
plt.show()
