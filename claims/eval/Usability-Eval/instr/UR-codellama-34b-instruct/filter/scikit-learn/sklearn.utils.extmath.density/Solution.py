import numpy as np
from sklearn.preprocessing import normalize
from sklearn.metrics import accuracy_score
from sklearn.metrics.pairwise import pairwise_distances

# Generate a random sparse vector
n_samples = 100
n_features = 10
sparse_vector = np.random.randint(2, size=(n_samples, n_features))

# Compute the density of the sparse vector using sklearn
density = sparse_vector.toarray().sum() / (n_samples * n_features)

print("The density of the sparse vector is:", density)
