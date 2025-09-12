import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Example data
X = np.random.rand(100, 64)

# Initialize MiniBatchDictionaryLearning
dict_learner = MiniBatchDictionaryLearning(
    n_components=50,  # Number of dictionary elements
    alpha=1.0,        # Regularization parameter
    n_iter=1000,      # Number of iterations to perform
    batch_size=10,    # Size of the mini-batches
    random_state=42
)

# Fit the model
dict_learner.fit(X)

# The dictionary learned from the data
D = dict_learner.components_

# Transform data into sparse codes
codes = dict_learner.transform(X)

print("Dictionary shape:", D.shape)
print("Codes shape:", codes.shape)
