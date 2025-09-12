import numpy as np
from sklearn.decomposition import DictionaryLearning
from sklearn.utils import gen_batches

# Example data
X = np.random.rand(100, 20)  # 100 samples, 20 features

# Initialize DictionaryLearning model
dict_learner = DictionaryLearning(n_components=10, transform_algorithm='lars', random_state=42)

# Online learning using partial_fit
for batch in gen_batches(X.shape[0], batch_size=10):
    dict_learner.partial_fit(X[batch])

# Transform the data using the learned dictionary
X_transformed = dict_learner.transform(X)

# Get the learned dictionary
dictionary = dict_learner.components_

print("Learned Dictionary:\n", dictionary)
print("Transformed Data:\n", X_transformed)
