from sklearn.decomposition import MiniBatchDictionaryLearning

# Assuming you have your data as a 2D numpy array
import numpy as np
data = np.random.rand(100, 20)  # Example data

# Initialize the MiniBatchDictionaryLearning model
dictionary_learning = MiniBatchDictionaryLearning(n_components=10, max_iter=100, random_state=42)

# Fit the model to the data
dictionary_learning.fit(data)

# Get the learned dictionary
atoms = dictionary_learning.components_

print("Learned Dictionary Atoms:")
print(atoms)
