from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling for better accuracy
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create the RadiusNeighborsClassifier model with a specific radius
radius_neighbors_classifier = RadiusNeighborsClassifier(radius=1.0)

# Fit the model on the training data
radius_neighbors_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred = radius_neighbors_classifier.predict(X_test_scaled)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
