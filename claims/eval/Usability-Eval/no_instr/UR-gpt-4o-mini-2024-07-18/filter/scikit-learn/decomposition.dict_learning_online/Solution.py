import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Generate some sample data
np.random.seed(0)
data = np.random.rand(100, 30)  # 100 samples with 30 features

# Define parameters for dictionary learning
n_components = 10  # Number of dictionary elements
n_iter = 100  # Number of iterations
batch_size = 10  # Size of mini-batches

# Initialize and fit the MiniBatchDictionaryLearning model
dictionary_learner = MiniBatchDictionaryLearning(n_components=n_components, n_iter=n_iter, batch_size=batch_size)
dictionary = dictionary_learner.fit_transform(data)

# Display the learned dictionary
print("Learned dictionary:")
print(dictionary_learner.components_)
