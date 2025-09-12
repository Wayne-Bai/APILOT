from sklearn.datasets import load_boston

# Load the Boston house-prices dataset
boston_dataset = load_boston()

# Access the features and target
features = boston_dataset.data
target = boston_dataset.target

# Display dataset information
feature_names = boston_dataset.feature_names
print("Feature names:", feature_names)
print("Data shape:", features.shape)
print("Target shape:", target.shape)
