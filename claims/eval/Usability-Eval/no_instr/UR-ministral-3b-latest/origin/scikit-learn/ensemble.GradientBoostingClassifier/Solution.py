import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a synthetic classification dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Gradient Boosting classifier
gb_classifier = GradientBoostingClassifier(n_estimators=100, random_state=42, max_depth=3)

# Train the classifier with the training data
gb_classifier.fit(X_train, y_train)

# Predict the classes for the testing data
y_pred = gb_classifier.predict(X_test)

# Compute the accuracy of the classifier on the testing data
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
