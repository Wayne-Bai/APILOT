import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Create a sparse random signal
rng = np.random.RandomState(42)
n_samples, n_features = 100, 50
n_components = 30
data = rng.randn(n_samples, n_features)
data[:, ::2] += 3 * rng.randn(n_samples, n_features // 2)

# Initialize MiniBatchDictionaryLearning
mb_dict_learning = MiniBatchDictionaryLearning(
    n_components=n_components,
    alpha=1,
    n_iter=500,
    batch_size=10,
    random_state=42
)

# Fit the model to the data
V = mb_dict_learning.fit_transform(data)

# Output the components (dictionary) and the code (sparse representation)
dictionary = mb_dict_learning.components_

# Printing results
print("The learned dictionary (components):\n", dictionary)
print("Sparse code representation:\n", V)
