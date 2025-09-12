from sklearn.decomposition import DictionaryLearning
import numpy as np

# Example usage
# Generating some data
n_items, n_topics = 10, 5
data = np.random.rand(n_items, n_topics)

# Initialize Dictionary Learning model
dl = DictionaryLearning(n_components=n_topics)

# Fit the model
dl.fit(data)

# Predict dictionary matrix
dict_matrix = dl.components_

# Predict the dense matrix
dense_matrix = dl.transform(data)
