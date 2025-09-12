import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn.utils import gen_batches

# Example data
X = np.random.rand(100, 50)  # 100 samples, 50 features

# Initialize the DictionaryLearning model
dict_learner = DictionaryLearning(n_components=10, batch_size=10, max_iter=100, random_state=42)

# Mini-batch dictionary learning
for batch in gen_batches(X.shape[0], batch_size=dict_learner.batch_size):
    dict_learner.partial_fit(X[batch])

# Get the learned dictionary
dictionary = dict_learner.components_

print("Learned Dictionary:")
print(dictionary)
