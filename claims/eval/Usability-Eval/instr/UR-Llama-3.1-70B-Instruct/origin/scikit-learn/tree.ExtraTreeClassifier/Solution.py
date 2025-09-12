# Import necessary libraries
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Import dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create an Extremely Randomized Tree Classifier
ert_classifier = ExtraTreesClassifier(n_estimators=100, random_state=1)

# Train the model using the training sets
ert_classifier = ert_classifier.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = ert_classifier.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:", accuracy_score(y_test, y_pred))

# Model Precision and Recall
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Model Confusion matrix
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))
