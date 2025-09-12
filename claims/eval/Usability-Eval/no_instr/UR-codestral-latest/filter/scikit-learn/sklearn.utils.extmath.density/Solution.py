from scikit_learn.feature_extraction.text import CountVectorizer
import numpy as np

# Let's assume we have the following sparse vector
sparse_vector = ["this is a sample text"]

# Initialize the CountVectorizer object
vectorizer = CountVectorizer()

# Create the sparse matrix
X = vectorizer.fit_transform(sparse_vector)

# Compute the density of the sparse matrix
density = X.nnz / float(X.shape[0] * X.shape[1])

print("Density of the sparse vector is:", density)
