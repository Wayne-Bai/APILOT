import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Initialize a sparse mini-batch dictionary learning model
model = MiniBatchDictionaryLearning(n_components=100, iter=10, random_state=42)

# Fit the model on input data
model.fit(data)

# The learned dictionary (or the seed dictionary if 'fitting initialization' is set to True)
dictionary = model.components_

# Transform the data using the learned dictionary
transformed_data = model.transform(data)
