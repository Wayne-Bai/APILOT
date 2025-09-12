import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Sample data: Replace with your actual data
X = np.random.rand(100, 64)  # 100 samples, 64 features each

# Parameters
n_components = 50  # number of dictionary elements - adjust to your needs

dict_learner = MiniBatchDictionaryLearning(n_components=n_components, 
                                           n_iter=500,
                                           batch_size=3,
                                           random_state=0)

V = dict_learner.fit_transform(X)

# V contains the code (sparse representation)
# dict_learner.components_ contains the components (dictionary atoms)

print("Dictionary Components:")
print(dict_learner.components_)

print("Code (sparse representation):")
print(V)
