from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

# Load iris dataset as an example
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize PLSRegression model
pls = PLSRegression(n_components=2)

# Fit the model to the training data
pls.fit(X_train, y_train)

# Make predictions on the test data
y_pred = pls.predict(X_test)

# Print the predicted targets
print("Predicted targets:", y_pred)
