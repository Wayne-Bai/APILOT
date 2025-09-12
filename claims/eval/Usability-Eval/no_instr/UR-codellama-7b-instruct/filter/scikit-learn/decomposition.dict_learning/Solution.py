
import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a random matrix
X = np.random.rand(10, 20)

# Initialize the dictionary learning object
dl = DictionaryLearning()

# Fit the dictionary to the data
dl.fit(X)

# Print the dictionary
print(dl.dictionary_)
