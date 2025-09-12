from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
sparse_vector = np.array([0, 0, 1, 0, 0])
density = 1 - cosine_similarity(sparse_vector)
print(density)
