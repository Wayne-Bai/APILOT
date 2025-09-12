from sklearn.preprocessing import OneHotEncoder

# Assume X is your categorical features and y is your target variable

# Initialize OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the categorical features
X_encoded = encoder.fit_transform(X)

# Get the feature names from the encoder
feature_names = encoder.get_feature_names(['cat', 'dog', 'bird'])

# Print the encoded features and their corresponding names
print("Encoded Features:\n", X_encoded.toarray())
print("\nFeature Names:\n", feature_names)
