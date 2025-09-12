from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Assuming that X is your data matrix
X = np.random.rand(100, 100)

# Create a dictionary learning object with 2 atoms (elements in the dictionary)
dictionary_learning = MiniBatchDictionaryLearning(n_components=2, random_state=0)

# Fit the dictionary learning model to the data
X_dict = dictionary_learning.fit(X)

# X_dict is the new representation of X where it is approximated by a linear combination
# of the learned dictionary elements.
