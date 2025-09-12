from sklearn.ensemble import HistogramGradientBoostingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Histogram Gradient Boosting Classifier
hgb = HistogramGradientBoostingClassifier(max_iter=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the classifier to the training data
hgb.fit(X_train, y_train)

# Predict the labels of the test data
y_pred = hgb.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
