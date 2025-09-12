import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Define the dataset and the target variable
X = ... # Feature data
y = ... # Target data

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the radius for the nearest neighbors search
radius = 0.5

# Create a NearestNeighbors object and fit it to the training data
nbrs = NearestNeighbors(radius=radius).fit(X_train)

# Find the neighbors for each sample in the test set
neighbors = nbrs.kneighbors(X_test, return_distance=False)

# Create a empty list to store the predicted labels
predicted_labels = []

for i in range(len(X_test)):
    # Get the neighbors for the current sample
    neighbor_labels = y_train[neighbors[i]]
    
    # Calculate the majority vote among the neighbors
    predicted_label = np.argmax(np.bincount(neighbor_labels))
    
    # Append the predicted label to the list
    predicted_labels.append(predicted_label)

# Evaluate the performance of the classifier using accuracy score, classification report and confusion matrix
accuracy = accuracy_score(y_test, predicted_labels)
print("Accuracy: ", accuracy)

report = classification_report(y_test, predicted_labels)
print("Classification Report: \n", report)

cm = confusion_matrix(y_test, predicted_labels)
print("Confusion Matrix: \n", cm)
