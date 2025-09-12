from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate some random data
X = np.random.rand(100, 200)

# Initialize the MiniBatchDictionaryLearning object
mbdl = MiniBatchDictionaryLearning(n_components=10, batch_size=20, alpha=0.1, n_iter=1000, fit_algorithm='lars', random_state=42)

# Fit the model to the data
mbdl.fit(X)

# Transform the data using the learned dictionary
X_transformed = mbdl.transform(X)

# Print the shape of the transformed data
print(X_transformed.shape)
