import numpy as np
from sklearn.decomposition import PCA

# Example data
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize PCA with the desired number of components
pca = PCA(n_components=2, svd_solver='full')

# Fit PCA to the data
pca.fit(data)

# Transform the data to the lower dimensional space
transformed_data = pca.transform(data)

print("Original data:\n", data)
print("Transformed data:\n", transformed_data)
