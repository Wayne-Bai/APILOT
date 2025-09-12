from sklearn.decomposition import DictionaryLearning

# Assuming X is your data matrix
dl = DictionaryLearning(n_components=100, random_state=0)
dl.fit(X)

# Now dl.components_ holds the dictionary (set of "atoms")
print(dl.components_)
