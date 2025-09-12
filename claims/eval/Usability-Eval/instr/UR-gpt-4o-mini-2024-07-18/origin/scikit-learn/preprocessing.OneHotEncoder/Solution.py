from sklearn.preprocessing import OneHotEncoder

# Sample data
data = [['cat'], ['dog'], ['cat'], ['bird']]

# Create the OneHotEncoder instance
encoder = OneHotEncoder(sparse=False)

# Fit and transform the data
one_hot_encoded = encoder.fit_transform(data)

# Display the result
print(one_hot_encoded)
