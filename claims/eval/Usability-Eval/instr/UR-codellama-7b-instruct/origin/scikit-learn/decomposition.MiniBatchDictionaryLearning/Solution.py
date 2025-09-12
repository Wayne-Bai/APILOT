from sklearn.feature_extraction import DictLearning
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the dictionary learning algorithm
dl = DictLearning(n_components=5)

# Fit the model to the training data
dl.fit(X_train)

# Evaluate the model on the testing data
y_pred = dl.predict(X_test)
score = accuracy_score(y_test, y_pred)
print("Accuracy:", score)
