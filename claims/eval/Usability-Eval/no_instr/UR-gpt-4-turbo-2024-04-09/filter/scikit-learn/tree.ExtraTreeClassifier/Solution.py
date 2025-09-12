from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Extremely Randomized Trees Classifier
extremely_randomized_tree = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Train the classifier
extremely_randomized_tree.fit(X_train, y_train)

# Make predictions
predictions = extremely_randomized_tree.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')
