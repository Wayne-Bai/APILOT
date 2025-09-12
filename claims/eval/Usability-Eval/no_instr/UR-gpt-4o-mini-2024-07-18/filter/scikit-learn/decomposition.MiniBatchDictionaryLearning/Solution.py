from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate some synthetic data for demonstration
X = np.random.rand(100, 20)

# Set the parameters for MiniBatchDictionaryLearning
n_components = 10  # Number of atoms in the dictionary
batch_size = 5     # Size of mini-batches

# Initialize and fit the model
dictionary_learner = MiniBatchDictionaryLearning(n_components=n_components, batch_size=batch_size)
V = dictionary_learner.fit(X).components_

# Display the learned dictionary
print("Learned dictionary (components):\n", V)
