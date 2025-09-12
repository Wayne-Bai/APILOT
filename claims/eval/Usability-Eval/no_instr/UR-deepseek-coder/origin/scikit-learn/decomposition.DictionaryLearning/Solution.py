import numpy as np
from sklearn.decomposition import DictionaryLearning

# Generate some example data
X = np.random.rand(100, 50)  # 100 samples, 50 features

# Initialize the DictionaryLearning model
dict_learner = DictionaryLearning(n_components=10, max_iter=100, transform_algorithm='omp', random_state=42)

# Fit the model to the data
dict_learner.fit(X)

# Get the learned dictionary
dictionary = dict_learner.components_

# Transform the data using the learned dictionary
X_transformed = dict_learner.transform(X)

print("Learned Dictionary:")
print(dictionary)

print("\nTransformed Data:")
print(X_transformed)
