from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate some random data
n_samples, n_features = 1000, 500
X = np.random.randn(n_samples, n_features)

# Initialize the MiniBatchDictionaryLearning object
n_atoms = 100
dictionary_size = n_atoms
batch_size = 50
max_iter = 100

# Fit the model
dict_learn = MiniBatchDictionaryLearning(
    n_components=n_atoms,
    alpha=1,
    n_iter=max_iter,
    batch_size=batch_size,
    shuffle=True,
    random_state=42
)

# Transform the data
D = dict_learn.fit_transform(X)

# Get the learned dictionary
dictionary = dict_learn.components_
