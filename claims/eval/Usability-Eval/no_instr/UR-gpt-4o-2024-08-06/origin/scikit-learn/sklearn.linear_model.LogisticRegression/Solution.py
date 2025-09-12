import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample data: Features (X) and labels (y)
# Here, we assume X is a 2D numpy array with shape (n_samples, n_features)
# and y is a 1D numpy array with shape (n_samples,).
X = np.array([[1.2, 3.1], [1.9, 2.3], [4.5, 5.6], [3.4, 4.5], [3.1, 0.9], [0.2, 1.8]])
y = np.array([0, 0, 1, 1, 0, 0])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
