import numpy as np
from sklearn.decomposition import SparsePCA

# Create example data
data = np.random.rand(100, 10)  # 100 samples with 10 features each

# Instantiate a SparsePCA model
sparse_pca = SparsePCA(n_components=5, alpha=0.8, random_state=42)

# Fit the model with the data
sparse_pca.fit(data)

# Transform the data according to the sparse components
components = sparse_pca.transform(data)

# Get the extracted sparse components
sparse_components = sparse_pca.components_

print("Extracted Sparse Components:")
print(sparse_components)
