import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Example data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize the MiniBatchDictionaryLearning model
dict_learner = MiniBatchDictionaryLearning(n_components=3, alpha=1, batch_size=2, n_iter=100)

# Fit the model to the data
dict_learner.fit(X)

# Get the learned dictionary
dictionary = dict_learner.components_

print("Learned Dictionary:")
print(dictionary)
