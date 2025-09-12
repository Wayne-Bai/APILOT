from sklearn.decomposition import MiniBatchDictionaryLearning

# Assuming X is your data matrix
# Initialize the dictionary learning object
dictionary_learning = MiniBatchDictionaryLearning(n_components=100, alpha=0.1, n_iter=100, batch_size=10, random_state=42)

# Fit the model to your data
dictionary_learning.fit(X)

# Now, dictionary_learning.components_ will contain the learned dictionary
