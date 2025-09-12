from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import RadiusNeighborsClassifier

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Create a RadiusNeighborsClassifier
clf = RadiusNeighborsClassifier(radius=5.0, outlier_label=-1)

# Train the classifier
clf.fit(X_train, y_train)

# Use the classifier to make predictions on the test data
y_pred = clf.predict(X_test)
