from sklearn.naive_bayes import GaussianNB
import numpy as np

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Example of training data
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 1, 0, 1])

# Initial fit of the model
gnb.partial_fit(X_train, y_train, classes=np.unique(y_train))

# Example of new data for online update
X_new = np.array([[5, 6], [6, 7]])
y_new = np.array([1, 0])

# Online update of the model
gnb.partial_fit(X_new, y_new)

# Example of prediction with the updated model
predictions = gnb.predict(np.array([[7, 8], [2, 1]]))
print(predictions)
