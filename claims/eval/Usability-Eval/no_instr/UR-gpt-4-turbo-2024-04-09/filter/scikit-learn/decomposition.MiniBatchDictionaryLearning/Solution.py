import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Creating some sample data
X = np.random.rand(100, 10)  # 100 samples, 10 features each

# Instantiate MiniBatchDictionaryLearning
n_components = 15  # number of dictionary elements - usually less than number of features
dict_learner = MiniBatchDictionaryLearning(n_components=n_components, batch_size=10, n_iter=500)

# Fit the model
V = dict_learner.fit(X).components_

# V is the matrix of the dictionary atoms
print("Dictionary atoms:")
print(V)
