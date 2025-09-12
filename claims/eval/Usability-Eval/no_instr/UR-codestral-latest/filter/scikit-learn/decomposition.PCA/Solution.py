from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Assuming you have data in 'data' variable
# Center the data (mean = 0) but do not scale each feature
centered_data = data - data.mean(axis=0)

# Create PCA object
pca = PCA()

# Fit and apply dimensionality reduction on centered data
reduced_data = pca.fit_transform(centered_data)

# Print the explained variance ratio to understand how much information is retained in each principal component
print(pca.explained_variance_ratio_)
