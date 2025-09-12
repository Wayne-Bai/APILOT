import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Extreme decision tree classifier with 10 trees and maximum depth of 3
clf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)

# Train the model on training data
clf.fit(X_train, y_train)

# Make predictions on test data
predictions = clf.predict(X_test)

# Evaluate performance of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
