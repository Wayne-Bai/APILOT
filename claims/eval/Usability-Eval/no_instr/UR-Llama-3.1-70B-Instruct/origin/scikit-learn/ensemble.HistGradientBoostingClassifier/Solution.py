# Importing necessary libraries from scikit-learn
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset (Breast Cancer)
data = load_breast_cancer()
X = data.data
y = data.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Histogram-based Gradient Boosting Classification Tree
hgbdt = HistGradientBoostingClassifier(random_state=42)

# Train the model using the training sets
hgbdt.fit(X_train, y_train)

# Make predictions using the test set
y_pred = hgbdt.predict(X_test)

# Model Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Other metrics
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
