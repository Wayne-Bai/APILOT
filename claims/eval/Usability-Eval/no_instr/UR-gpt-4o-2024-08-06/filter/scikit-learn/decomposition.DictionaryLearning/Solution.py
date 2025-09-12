from sklearn.decomposition import DictionaryLearning
import numpy as np

# Example data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a DictionaryLearning model
# n_components: Number of dictionary elements
# alpha: Sparsity controlling parameter
# max_iter: Maximum number of iterations
dict_learn = DictionaryLearning(n_components=2, alpha=1, max_iter=1000, random_state=42)

# Fit the model to the data
X_transformed = dict_learn.fit_transform(X)

# Retrieve the dictionary atoms and the sparse code
dictionary_atoms = dict_learn.components_
sparse_code = X_transformed

# Print the results
print("Dictionary Atoms:\n", dictionary_atoms)
print("Sparse Code:\n", sparse_code)
