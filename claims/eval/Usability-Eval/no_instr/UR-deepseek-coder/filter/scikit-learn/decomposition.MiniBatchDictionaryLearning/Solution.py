import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.datasets import make_sparse_coded_signal

# Generate synthetic sparse coded signal
n_components, n_features = 50, 100
n_nonzero_coefs = 10
data, dictionary, code = make_sparse_coded_signal(n_samples=1000, 
                                                  n_components=n_components, 
                                                  n_features=n_features, 
                                                  n_nonzero_coefs=n_nonzero_coefs)

# Initialize MiniBatchDictionaryLearning
dict_learner = MiniBatchDictionaryLearning(n_components=n_components, 
                                           alpha=1.0, 
                                           n_iter=500, 
                                           batch_size=3, 
                                           shuffle=True, 
                                           random_state=42)

# Fit the model
dict_learner.fit(data)

# Transform the data
transformed_data = dict_learner.transform(data)

# Reconstruct the original data
reconstructed_data = np.dot(transformed_data, dict_learner.components_)

# Print the results
print("Original Data Shape:", data.shape)
print("Transformed Data Shape:", transformed_data.shape)
print("Reconstructed Data Shape:", reconstructed_data.shape)
