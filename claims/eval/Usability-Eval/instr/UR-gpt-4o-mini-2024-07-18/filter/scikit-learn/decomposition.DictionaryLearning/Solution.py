import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Generate sample data
np.random.seed(0)
data = np.random.rand(100, 50)  # 100 samples, 50 features

# Set parameters
n_atoms = 10  # Number of dictionary atoms
n_components = 5  # Size of the sparse representation

# Dictionary learning
dictionary_learning = MiniBatchDictionaryLearning(n_components=n_atoms, batch_size=10, n_iter=100)
dictionary = dictionary_learning.fit(data).components_

# Transform the data into sparse representations
sparse_representation = dictionary_learning.transform(data)

print("Dictionary (atoms):")
print(dictionary)
print("\nSparse representation:")
print(sparse_representation)
