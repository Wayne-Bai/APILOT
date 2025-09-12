# Import the necessary module
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generating a sample dataset
X = np.random.rand(100, 10)

# Create a MiniBatchDictionaryLearning instance and specify parameters
dictionary_learning = MiniBatchDictionaryLearning(n_components=2, n_iter=10)

# Fit to the data and transform
dictionary = dictionary_learning.fit(X)

# Get the code words (dictionary components)
code_words = dictionary.components_

# Get the code (representation of X in the dictionary basis)
code = dictionary.transform(X)
