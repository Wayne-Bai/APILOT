import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate a sample data matrix
data = np.random.rand(100, 50)

# Initialize the DictionaryLearning model
dl = DictionaryLearning(n_components=10, max_iter=1000, fit_algorithm='lars', transform_algorithm='lasso_lars')

# Fit the model to the data
dl.fit(data)

# Transform the data to obtain the sparse code
sparse_code = dl.transform(data)

# The dictionary (atoms) learned by the model
dictionary = dl.components_

print("Dictionary (atoms):\n", dictionary)
print("Sparse code:\n", sparse_code)
