from sklearn.naive_bayes import GaussianNB
import numpy as np

# Create the Gaussian Naive Bayes model
model = GaussianNB()

# Sample training data - features (X) and labels (y)
X_train = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [6.0, 9.0]])
y_train = np.array([0, 0, 1, 1])

# Fit the model on the initial dataset
model.fit(X_train, y_train)

# New data for online updates
X_new = np.array([[1.2, 1.7], [5.5, 8.5]])
y_new = np.array([0, 1])

# Perform online updates to the model using partial_fit
model.partial_fit(X_new, y_new, classes=np.unique(y_train))
