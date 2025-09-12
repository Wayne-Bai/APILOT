import numpy as np
from sklearn.decomposition import PCA

# Sample data: replace this with your actual data
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

# Center the data (mean subtraction)
mean = np.mean(data, axis=0)
centered_data = data - mean

# Apply PCA
pca = PCA(n_components=1)  # Reduce to 1 dimension
principal_components = pca.fit_transform(centered_data)

# Output the principal components
print("Principal Components:\n", principal_components)
