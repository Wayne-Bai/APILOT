from sklearn.decomposition import MiniBatchDictionaryLearning

# Dictionary learning matrix factorization
# Create a new MiniBatchDictionaryLearning object
dictionary_learning = MiniBatchDictionaryLearning(n_components=10, alpha=1, n_iter=500)

# Fit the model to the data. X is your data matrix.
dictionary_learning.fit(X)

# Use the components_ attribute to get the learned dictionary
dictionary = dictionary_learning.components_
