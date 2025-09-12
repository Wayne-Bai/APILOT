# Import necessary libraries from scikit-learn
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

# Load a dataset
iris = load_iris()

# Define features and target
X = iris.data
y = iris.target

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of RadiusNeighborsClassifier
rnn = RadiusNeighborsClassifier(radius=8.0)

# Train the model
rnn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rnn.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
