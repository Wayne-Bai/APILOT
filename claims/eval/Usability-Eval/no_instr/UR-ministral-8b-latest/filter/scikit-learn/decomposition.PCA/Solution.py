import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Assuming 'data' is your input data as a 2D numpy array or pandas DataFrame
# Example: data = np.array([[1, 2], [3, 4], [5, 6]])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Apply PCA
pca = PCA(n_components=None)  # Use 'n_components=None' to keep all components
pca_result = pca.fit_transform(scaled_data)

print("Original data shape:", data.shape)
print("PCA transformed data shape:", pca_result.shape)
