from sklearn.preprocessing import OneHotEncoder

# Example data
categories = [
    ['red'], ['green'], ['blue'], ['green'], ['red']
]

# Creating the OneHotEncoder instance
encoder = OneHotEncoder(sparse=False)

# Fitting and transforming the data to one-hot encode
encoded_categories = encoder.fit_transform(categories)

print("Encoded categories:")
print(encoded_categories)
