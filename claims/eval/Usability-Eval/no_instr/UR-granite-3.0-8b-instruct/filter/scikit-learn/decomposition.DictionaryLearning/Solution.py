from sklearn.decomposition import MiniBatchDictionaryLearning

# Assuming X is your data
dictionary_learning = MiniBatchDictionaryLearning(n_components=100, alpha=0.1, n_iter=1000)
dictionary_learning.fit(X)

# To get the dictionary
dictionary = dictionary_learning.components_
