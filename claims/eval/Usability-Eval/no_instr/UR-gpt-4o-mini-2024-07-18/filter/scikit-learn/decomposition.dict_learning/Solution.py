import numpy as np
from sklearn.decomposition import DictionaryLearning

# Sample data (feature matrix) X
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [1, 0, 1]])

# Create a DictionaryLearning model
n_components = 2  # Number of dictionary components
dict_learner = DictionaryLearning(n_components=n_components, transform_algorithm='lasso', random_state=0)

# Fit the model to the data
X_transformed = dict_learner.fit_transform(X)

# Get the dictionary
dictionary = dict_learner.components_

# Output the results
print("Transformed Data:\n", X_transformed)
print("Learned Dictionary:\n", dictionary)
