from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Example dataset
X = np.array([
    [1, 2, 0],
    [0, 1, 1],
    [1, 0, 2],
    [2, 1, 0],
    [0, 2, 1],
    [1, 1, 2]
])

y = np.array([0, 1, 0, 1, 0, 1])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Categorical Naive Bayes classifier
clf = CategoricalNB()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print detailed classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))
