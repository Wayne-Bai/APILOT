from sklearn.decomposition import DictionaryLearning
from sklearn.datasets import make_sparse_image
from sklearn.datasets import fetch_hastie_57
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Load sample data (optional)
# X, Y = make_sparse_image(image_size=(100, 100), noise=0.1, force-positive=True, random_state=42)
X, Y = fetch_hastie_57().data, fetch_hastie_57().target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create Dictionary Learning object with the number of atoms set to 64
dictionary.learning_algorithm ='mod ALS'
dictionary = DictionaryLearning(n_components=64, fit_algorithm='lars',
                                solver='lars', MAXITER=5000, tol=1e-6)

# Fit the dictionary to the training data
dictionary.fit(X_train)

# Get the learned dictionary and the coefficients
dictionary_tuple = dictionary.components_, dictionary.coef_

# Print the recovered dictionary and coefficients
print("Learned Dictionary:", dictionary_tuple[0])
print("Coefficients:", dictionary_tuple[1])

# Reconstruct the data using the learned dictionary and coefficients
X_reconstructed = dictionary.transform(X_test)

# Calculate the mean squared error
mse = mean_squared_error(Y_test, X_reconstructed)

# Print the mean squared error
print("Mean Squared Error:", mse)

# Visualize the original and reconstructed images
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(np.reshape(X_test[0, :], (10, 10)))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(np.reshape(X_reconstructed[0, :], (10, 10)))
plt.title("Reconstructed Image")
plt.show()
