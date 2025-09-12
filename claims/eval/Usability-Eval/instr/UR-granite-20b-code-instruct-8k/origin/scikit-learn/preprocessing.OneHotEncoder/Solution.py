from sklearn.preprocessing import OneHotEncoder

# create an instance of OneHotEncoder
encoder = OneHotEncoder()

# fit and transform the data
onehot = encoder.fit_transform(data)
