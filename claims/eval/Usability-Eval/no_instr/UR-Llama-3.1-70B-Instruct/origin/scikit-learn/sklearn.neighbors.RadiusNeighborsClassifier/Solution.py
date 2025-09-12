# Import necessary libraries
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load iris dataset
iris = load_iris()

# Split dataset into features and target variable
X = iris.data
y = iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create a RadiusNeighborsClassifier object with a radius of 10
radius_neighbors_clf = RadiusNeighborsClassifier(radius=10.0)

# Train the classifier using the training data
radius_neighbors_clf.fit(X_train, y_train)

# Predict the test data using the trained classifier
y_pred = radius_neighbors_clf.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Print the classification report
print("Classification Report:\n", classification_report(y_test, y_pred))
