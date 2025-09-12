import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
data = fetch_openml(name='adult', version='latest')
X, y = data['data'], data['target']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create K-Nearest Neighbors Classifier
knn = KNeighborsClassifier(n_neighbors=3, algorithm='kd_tree')

# Fit the model using training data
knn.fit(X_train, y_train)

# Make predictions
predictions = knn.predict(X_test)

print(predictions)
