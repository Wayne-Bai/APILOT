
import numpy as np
from sklearn.decomposition import DictionaryLearning

# Assume you have a matrix X with shape (n_samples, n_features)
# n_samples is the number of samples in your dataset
# n_features is the number of features per sample
# n_components is the number of dictionary atoms in the dictionary

n_samples = 100
n_features = 3
n_components = 2

# Generate some data for an example
data = np.random.rand(n_samples, n_features)

# Initialize the DictionaryLearning object
dico_learner = DictionaryLearning(n_components=n_components)

# Apply the dictionary learning to the data
dico = dico_learner.fit_transform(data)

# Output the learned dictionary and transformed data
print("Learned dictionary:")
print(dico_learner.components_)
print("\nTransformed data:")
print(dico)
