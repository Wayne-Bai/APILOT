from sklearn.decomposition import DictionaryLearning
import numpy as np

# Example data: create a random matrix with 100 samples and 10 features
X = np.random.rand(100, 10)

# Initialize the DictionaryLearning model
dict_learner = DictionaryLearning(n_components=5, fit_algorithm='lars', transform_algorithm='omp')

# Fit the model with the data
dictionary = dict_learner.fit(X)

# Transform data using the learned dictionary
transformed_data = dict_learner.transform(X)

print("Learned dictionary components:")
print(dictionary.components_)

print("Transformed data:")
print(transformed_data)
