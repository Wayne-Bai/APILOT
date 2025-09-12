from sklearn. MiniBatchDictionaryLearning import MiniBatchDictionaryLearning

# Create aMini-batch dictionary learning object
dict_learning = MiniBatchDictionaryLearning(n_components=10, alpha=0.1, n_iter=50,
 batch_size=3, random_state=0)

# Fit the model to the data
dictionary = dict_learning.fit(X)

# Transform the data into the learned dictionaries
X_transformed = dict_learning.transform(X)
