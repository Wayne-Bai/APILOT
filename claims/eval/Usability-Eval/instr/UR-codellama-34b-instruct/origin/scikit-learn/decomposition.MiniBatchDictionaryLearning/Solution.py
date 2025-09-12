from sklearn.linear_model import MiniBatchDictionaryLearning
import numpy as np

# Generate some sample data
n_samples, n_features = 100, 50
X = np.random.rand(n_samples, n_features)

# Initialize the mini-batch dictionary learning object
mbdl = MiniBatchDictionaryLearning(n_components=5, alpha=1e-3, batch_size=32)

# Perform dictionary learning on the data
mbdl.fit(X)

# Get the learned dictionaries
dictionaries = mbdl.get_dictionaries()

# Print the dictionaries
print(dictionaries)
