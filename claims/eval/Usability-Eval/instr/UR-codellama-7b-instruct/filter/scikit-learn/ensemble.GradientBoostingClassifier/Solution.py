
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklint.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv("your_dataset.csv")

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop("target", axis=1), data["target"], test_size=0.2, random_state=42)

# Train a Gradient Boosting Classifier on the training set
gb_clf = GradientBoostingClassifier()
gb_clf.fit(X_train, y_train)

# Predict the class labels of the testing set
y_pred = gb_clf.predict(X_test)

# Evaluate the performance of the model using accuracy score, classification report, and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
