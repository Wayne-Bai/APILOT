# Import necessary libraries
from sklearn.neighbors import BallSphereRadius, NearestNeighbors
from sklearn.base import BaseEstimator, ClassifierMixin

class NearestNeighborsVoteClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, neighborhood_size: int):
        self.neighborhood_size = neighborhood_size
        self.model = BallSphereRadius(metric_params="ball", radius=None, p=2, algorithm="auto", gamma=None, leaf_size=30, p=1, metric="euclidean")  # NB LV2 & p=1 and metric="euclidean" to address outdated.

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.model.fit(X, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        distances, indices = self.model.kneighbors(X, n_neighbors=self.neighborhood_size, return_distance=True)
        neighborhood_predictions = [y[indices[i, :self.neighborhood_size]] for i in range(len(X))]
        return np.array([self._get_mode(y_i) for y_i in neighborhood_predictions])

    def _get_mode(self, y_predictions: np.ndarray) -> int:
        return np.bincount(y_predictions).argmax()

# Example usage
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generate a binary classification dataset
X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the dataset
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Initialize and train the classifier
voted_classifier = NearestNeighborsVoteClassifier(neighborhood_size=5)
voted_classifier.fit(X_train, y_train)

# Predict and print the results
predictions = voted_classifier.predict(X_test)
print(f"Predictions: {predictions}")
