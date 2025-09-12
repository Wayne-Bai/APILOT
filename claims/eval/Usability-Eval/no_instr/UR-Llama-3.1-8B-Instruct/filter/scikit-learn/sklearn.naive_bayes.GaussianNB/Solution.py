# Importing necessary libraries
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Train the model on the training data
gnb.partial_fit(X_train, y_train, classes=np.unique(y_train))

# Make predictions on the test data
y_pred = gnb.predict(X_test)

# Evaluate the model's performance
print("Accuracy:", gnb.score(X_test, y_test))

# Perform online updates to the model parameters
# Let's assume we want to add a new data point (x_new, y_new) to the training set
x_new = [[5.1, 3.5, 1.4, 0.2]]  # new feature vector
y_new = 0  # new target (class label)

# Update the model parameters using the new data point
gnb.partial_fit(x_new, [y_new], classes=np.unique(y_train))

# Make predictions on the updated training set
y_pred_update = gnb.predict(X_train)

# Evaluate the model's performance after updating the parameters
print("Accuracy after update:", gnb.score(X_test, y_test))
