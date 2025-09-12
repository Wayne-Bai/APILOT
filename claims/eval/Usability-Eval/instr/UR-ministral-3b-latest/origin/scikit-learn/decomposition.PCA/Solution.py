from sklearn.decomposition import PCA

# Assuming you have your data in a 2D array called 'data'
# data = ...

# Standardize features by removing the mean and scaling to unit variance
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# data_ standardized = scaler.fit_transform(data)

# Apply PCA to reduce dimensionality
pca = PCA(n_components=2)  # change n_components to the desired number of components
data_pca = pca.fit_transform(data)

# Now data_pca contains the data in the lower-dimensional space
# print(data_pca)  # you can print or visualize the transformed data
