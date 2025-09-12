from sklearn.preprocessing import OneHotEncoder

# Assuming X is your DataFrame containing categorical features
# and categorical features are columns you want to encode

# Select the columns you want to encode
categorical_features = ["feature1", "feature2"]

# Initialize OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the encoder on the categorical features
X_encoded = encoder.fit_transform(X[categorical_features])

# The encoded features are now in X_encoded
