from sklearn.decomposition import DictionaryLearning
import numpy as np

# Sample data: replace this with your actual data
X = np.random.rand(100, 10)  # 100 samples, 10 features each

# Initialize DictionaryLearning
dict_learner = DictionaryLearning(n_components=5, max_iter=500, random_state=0)

# Fit the model to the data
V = dict_learner.fit_transform(X)

# The components of the dictionary
dictionary = dict_learner.components_

# V contains the code or the representation of X in the dictionary
# dictionary contains the dictionary elements/components

print("Representation of the data (V):")
print(V)
print("\nDictionary components:")
print(dictionary)
