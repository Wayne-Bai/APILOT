from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors

# Load iris dataset as an example
iris = datasets.load_iris()
X = iris.data

# Split dataset into training set and test set
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Create a K-NN model
knn = NearestNeighbors(n_neighbors=1, algorithm='ball_tree')
knn.fit(X_train)

# Predicting sample indices from X_test that are closest to the training set.
distances, indices = knn.kneighbors(X_test)

# print the closest training sample indices of test samples
print(indices)
