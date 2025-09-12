import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Define the function for voting among neighbors within a given radius
def voting_classifier(arr, radius):
    neighbors_labels = []
    classifier = KNeighborsClassifier(n_neighbors=radius)
    for sample_index in range(len(arr)):
        # Extract features and labels
        features = arr[sample_index][:-2]
        label = arr[sample_index][-2]

        # Fit the classifier to the current sample
        classifier.fit([features], [label])

        # Predict the label for each neighbor
        for neighbor_index in range(sample_index - radius, sample_index + radius + 1):
            if neighbor_index != sample_index and 0 <= neighbor_index < len(arr):
                neighbor_features = arr[neighbor_index][:-2]
                neighbor_label = arr[neighbor_index][-2]
                neighbors_labels.append(classifier.predict([neighbor_features])[0])
    return {label: count for label, count in np.bincount(neighbors_labels).items() if count > 0}

# Example usage
arr = np.array([
    [[1.0, 2.0], 3, 1],  # Example data
    [[2.0, 2.0], 3, 1],
    [[1.0, 3.0], 2, 0]
])

# Specify the radius
radius = 1

# Get the voting among neighbors within the given radius
result = voting_classifier(arr, radius)
print(result)
