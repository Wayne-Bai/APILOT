import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Sample data - assume you have some dataset, X
# For demonstration purposes, we'll generate a random dataset
np.random.seed(0)
X = np.random.rand(100, 64)  # 100 samples, each with 64 features

# Define the dictionary learning model
# n_components corresponds to the number of dictionary atoms you want to learn
n_components = 30  # Adjust based on your requirements
dict_learning = MiniBatchDictionaryLearning(n_components=n_components, alpha=1, n_iter=500, batch_size=10)

# Fit the model to the data
V = dict_learning.fit(X).components_

# Transform the data using the learned dictionary
# This encodes the data using the learned dictionary
X_transformed = dict_learning.transform(X)

# Display the learned dictionary (components)
print("Learned dictionary (set of atoms):")
print(V)

# Display the transformed data
print("\nTransformed data:")
print(X_transformed)
