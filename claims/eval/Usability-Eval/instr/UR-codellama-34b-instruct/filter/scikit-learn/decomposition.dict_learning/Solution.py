import numpy as np
from sklearn.decomposition import DictionaryLearning

# Define the matrix to be factored
X = np.array([[1, 0], [0, 1]])

# Initialize a dictionary learning object with the specified parameters
dl = DictionaryLearning(n_components=2, max_iter=10)

# Perform dictionary learning on the matrix X
code = dl.fit_transform(X)

# Get the learned dictionary
dictionary = dl.components_

print("Dictionary:")
print(dictionary)
print("\nCode:")
print(code)
