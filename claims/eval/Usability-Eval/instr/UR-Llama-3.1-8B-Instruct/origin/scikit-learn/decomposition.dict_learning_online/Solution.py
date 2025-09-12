# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.dictionaries import MiniBatchDictionaryDictionaryLearning
import numpy as np

# Generate some random data for dictionary learning
np.random.seed(0)
n_samples, n_features = 1000, 20
data = np.random.randn(n_samples, n_features)

# Define the number of atoms in the dictionary
n_atoms = 50

# Define the batch size for mini-batch dictionary learning
batch_size = 100

# Perform online dictionary learning using MiniBatchDictionaryLearning
ml = MiniBatchDictionaryLearning(n_atoms=n_atoms, batch_size=batch_size, n_iter=1000, verbose=True)

# Fit the model to the data
ml.fit(data)

# Get the learned dictionary
dictionary = ml.components_

# Print the learned dictionary
print("Learned Dictionary:")
print(dictionary)

# Get the representation of the data using the learned dictionary
representation = ml.transform(data)

# Print the representation of the data
print("\nRepresentation of the Data:")
print(representation)
