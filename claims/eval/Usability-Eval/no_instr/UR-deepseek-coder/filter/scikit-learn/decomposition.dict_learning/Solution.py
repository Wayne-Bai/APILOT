import numpy as np
from sklearn.decomposition import DictionaryLearning

# Example data: Replace this with your actual data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Initialize the DictionaryLearning model
dict_learner = DictionaryLearning(n_components=3, max_iter=1000, random_state=42)

# Fit the model to the data
dict_learner.fit(X)

# Transform the data to obtain the sparse code
sparse_code = dict_learner.transform(X)

# Get the learned dictionary
dictionary = dict_learner.components_

print("Learned Dictionary:\n", dictionary)
print("Sparse Code:\n", sparse_code)
