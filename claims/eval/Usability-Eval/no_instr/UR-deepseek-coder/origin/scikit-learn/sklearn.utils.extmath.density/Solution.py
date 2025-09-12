from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Example sparse vector (in CSR format)
sparse_vector = TfidfVectorizer().fit_transform(["sample document"])

# Compute density
density = np.sum(sparse_vector.data) / (sparse_vector.shape[0] * sparse_vector.shape[1])

print(f"Density of the sparse vector: {density}")
