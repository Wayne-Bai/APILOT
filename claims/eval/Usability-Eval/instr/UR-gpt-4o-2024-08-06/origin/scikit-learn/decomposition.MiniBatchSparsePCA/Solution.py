import numpy as np
from sklearn.decomposition import SparsePCA
from sklearn.preprocessing import StandardScaler

# Example data
data = np.array([[2.5, 2.4],
                 [0.5, 0.7],
                 [2.2, 2.9],
                 [1.9, 2.2],
                 [3.1, 3.0],
                 [2.3, 2.7],
                 [2.0, 1.6],
                 [1.0, 1.1],
                 [1.5, 1.6],
                 [1.1, 0.9]])

# Standardizing the data
scaler = StandardScaler()
data_std = scaler.fit_transform(data)

# Create a SparsePCA instance with appropriate alpha
sparse_pca = SparsePCA(n_components=2, alpha=1, random_state=42)

# Fit the model and transform the data
components = sparse_pca.fit_transform(data_std)

# Output the sparse components
print("Sparse components:")
print(components)

# Inverse transform the components to reconstruct the data
reconstructed_data = sparse_pca.inverse_transform(components)

print("\nReconstructed data:")
print(reconstructed_data)
