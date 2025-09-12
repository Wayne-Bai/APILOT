Python
from sklearn.datasets import load_iris
from sklearn.ensemble import HistGradientBoostingClassifier

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define the classifier
clf = HistGradientBoostingClassifier()

# Fit the model to the data
clf.fit(X, y)

# Predict the class of new data
X_new = X[:5]
y_new = clf.predict(X_new)

print(y_new)
