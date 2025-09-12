import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate some synthetic data
X = np.random.randn(100, 50)  # 100 samples, 50 features

# Dictionary learning
n_components = 10  # Number of dictionaries (atoms) to learn
dict_learner = DictionaryLearning(n_components=n_components, transform_alpha=1, n_iter=100, random_state=0)
X_transformed = dict_learner.fit_transform(X)

# Retrieve the learned dictionary
dictionary = dict_learner.components_

print("Learned dictionary shape:", dictionary.shape)
print("Transformed data shape:", X_transformed.shape)
