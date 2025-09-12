from sklearn.preprocessing import OneHotEncoder

# Sample data with categorical features
data = [
    ["Red", "Small"],
    ["Blue", "Medium"],
    ["Green", "Large"],
    ["Blue", "Small"]
]

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the data to a one-hot encoded array
one_hot_encoded_data = encoder.fit_transform(data)

# Print the encoded data
print(one_hot_encoded_data)
