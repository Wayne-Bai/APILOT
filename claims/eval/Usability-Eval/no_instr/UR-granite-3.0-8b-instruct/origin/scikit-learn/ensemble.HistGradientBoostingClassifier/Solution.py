# Import necessary libraries
from sklearn.ensemble import HistogramGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Histogram-based Gradient Boosting Classifier
hgb = HistogramGradientBoostingClassifier(max_iter=100, learning_rate=0.1, max_depth=3)

# Fit the model to the training data
hgb.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = hgb.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
