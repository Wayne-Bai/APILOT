import numpy as np

from sklearn.decomposition import SparseCoder, SparsePCA, MiniBatchDictionaryLearning, DictionaryLearning

# Generate a random n-samples x m-features matrix, n > m
n, m = 200, 100
np.random.seed(0)
X = np.dot(np.random.random(size=(m, 3)), np.random.random(size=(3, n)))

# Sparse coding with l1 penalty
dictionary_learner = SparseCoder(dictionary=np.eye(m), transform_alpha=0.1, alpha=1)
X_sparse_coding = dictionary_learner.transform(X)

# Sparse PCA with lasso penalty
dictionary_learner = SparsePCA(n_components=m, alpha=0.1)
X_sparse_pca = dictionary_learner.fit_transform(X)

# Mini-batch sparse coder
dictionary_learner = MiniBatchDictionaryLearning(n_components=m, alpha=0.1)
X_mini_batch_sparse_coder = dictionary_learner.fit_transform(X)

# Online dictionary learner
# Note that this model is suited for partial fit, so we need to initialize the model with a dictionary
dictionary_learner = DictionaryLearning(n_components=5, alpha=0.1)
dictionary_learner.fit(X)
X_online_dictionary_learner = dictionary_learner.transform(X)
