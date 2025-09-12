from sklearn.decomposition import DictionaryLearning

# create a dictionary learning object
dictionary_learning = DictionaryLearning(n_components=10, atom_size=5)

# fit the dictionary to the data
dictionary = dictionary_learning.fit(X)

# transform the data into a lower-dimensional representation
X_transformed = dictionary_learning.transform(X)

# optionally, you can also fit the model in one step using the fit_transform method
X_transformed = dictionary_learning.fit_transform(X)
