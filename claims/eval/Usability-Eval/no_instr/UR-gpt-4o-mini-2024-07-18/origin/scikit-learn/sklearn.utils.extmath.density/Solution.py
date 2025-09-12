from sklearn.feature_extraction import DictVectorizer
import numpy as np

# Example sparse vector represented as a dictionary
sparse_vector_dict = {'feature1': 1.0, 'feature3': 2.0}  # 'feature2' is absent, representing 0

# Convert the dictionary to a sparse matrix
vectorizer = DictVectorizer(sparse=True)
sparse_vector = vectorizer.fit_transform([sparse_vector_dict])

# Compute density
density = sparse_vector.nnz / np.prod(sparse_vector.shape)
print("Density of the sparse vector:", density)
