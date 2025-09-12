import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Example data matrix
X = np.random.rand(100, 64)  # 100 samples, 64 features

# Initialize the MiniBatchDictionaryLearning model
n_components = 10  # Number of dictionary atoms
model = MiniBatchDictionaryLearning(n_components=n_components, n_iter=500, random_state=0)

# Fit the model to the data
V = model.fit_transform(X)

# Get the learned dictionary
D = model.components_

# Display the learned dictionary
print("Learned dictionary shape:", D.shape)
