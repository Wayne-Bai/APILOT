from sklearn.preprocessing import InverseTransform

# Example usage:
n_features = 5  # Define the number of features

# Let's assume `transformer` is your already fitted transformer object,
# e.g., transformers like StandardScaler, MinMaxScaler, etc.

# For demonstration, let's create a sample transformer:
from sklearn.decomposition import PCA

# Assuming you have `pca` object with fit and transform applied
pca = PCA(n_components=2)
transformed_data = pca.fit_transform([[1.0, 2.0, 3.0, 4.0, 5.0]])

# Then inverse transform the data to get back to the original feature space
inverted_data = InverseTransform(transformer=pca, n_features=n_features).transform(transformed_data)

print("Original Feature Space Data:", inverted_data)
