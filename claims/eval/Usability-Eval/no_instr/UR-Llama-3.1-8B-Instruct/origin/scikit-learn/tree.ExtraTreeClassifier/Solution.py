# Import necessary libraries from scikit-learn
from sklearn.ensemble import ExtremelyRandomizedTreesClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load iris dataset (example dataset for classification)
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Extremely Randomized Trees Classifier
etc = ExtremelyRandomizedTreesClassifier(n_estimators=10, random_state=42)

# Train the model with the training data
etc.fit(X_train, y_train)

# Make predictions on the test data
y_pred = etc.predict(X_test)

# Evaluate the model's performance
print("Model Accuracy: ", accuracy_score(y_test, y_pred))
print("Classification Report: ")
print(classification_report(y_test, y_pred))
print("Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))
