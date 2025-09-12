# Import necessary libraries
from sklearn.decomposition import PartialLeastSquares
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample regression dataset
np.random.seed(0)
X, y = make_regression(n_samples=1000, n_features=100, random_state=0)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a Partial Least Square SVD object
pls = PartialLeastSquares(n_components=10)

# Fit the model to the training data
pls.fit(X_train, y_train)

# Transform the data using the trained model
X_train_pls = pls.transform(X_train)
X_test_pls = pls.transform(X_test)

# Print the shape of the transformed data
print("shape of X_train_pls:", X_train_pls.shape)
print("shape of X_test_pls:", X_test_pls.shape)

# Plot the explained variance of the model
plt.plot(pls.explained_variance_ratio_)
plt.xlabel('Component #')
plt.ylabel('Explain variance ratio')
plt.show()

# Print the number of features used after using partial least squares SVD
print('Number of features used after partial least squares SVD:', X_train_pls.shape[1])
