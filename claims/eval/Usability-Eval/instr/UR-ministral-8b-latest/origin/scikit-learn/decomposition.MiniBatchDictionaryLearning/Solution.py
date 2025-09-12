import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Assuming data is a numpy array with shape (n_samples, n_features)
data = np.random.rand(100, 100)

# Initialize the MiniBatchDictionaryLearning object
mb_lda = MiniBatchDictionaryLearning(n_components=10, random_state=42)

# Fit the model
mb_lda.fit(data)

# Access the resulting components
components = mb_lda.components_
