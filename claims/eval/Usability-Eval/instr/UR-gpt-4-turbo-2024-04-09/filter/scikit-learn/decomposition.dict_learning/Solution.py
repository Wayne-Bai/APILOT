# Import necessary modules from scikit-learn
from sklearn.decomposition import DictionaryLearning
import numpy as np

# Create some example data
X = np.random.rand(100, 10)  # 100 samples, 10 features

# Define the Dictionary Learning model
dict_learner = DictionaryLearning(n_components=5, fit_algorithm='lars')

# Fit the model on the data
V = dict_learner.fit_transform(X)

# Display the components (dictionary atoms)
print("Dictionary Atoms:")
print(dict_learner.components_)

# Display the transformed (code) data
print("Transformed (code) data:")
print(V)
