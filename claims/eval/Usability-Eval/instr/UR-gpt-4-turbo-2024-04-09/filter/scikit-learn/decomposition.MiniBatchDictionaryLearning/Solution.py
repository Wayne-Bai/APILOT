import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_sparse_coded_signal

# Generate sample data
n_components, n_features = 100, 64  # number of dictionary elements and features
n_nonzero_coefs = 17  # sparsity of data

# Generate sparse signal
data, dictionary, code = make_sparse_coded_signal(
    n_samples=200,
    n_components=n_components,
    n_features=n_features,
    n_nonzero_coefs=n_nonzero_coefs,
    random_state=42
)

# Apply MiniBatchKMeans
n_dict_atoms = 100  # number of atoms in the dictionary
mbkmeans = MiniBatchKMeans(n_clusters=n_dict_atoms, batch_size=20, n_init=10, random_state=42)
mbkmeans.fit(data.T)

# Extracted dictionary atoms
extracted_dictionary = mbkmeans.cluster_centers_.T

print("Shape of the extracted dictionary:", extracted_dictionary.shape)
