import numpy as np
from sklearn.decomposition import MiniBatchDictionaryLearning

# Example data
X = np.random.rand(100, 64)  # 100 samples with 64 features each

# Initialize the MiniBatchDictionaryLearning
n_components = 30  # Number of dictionary elements
batch_size = 10    # Size of batch for each iteration

dictionary_learning = MiniBatchDictionaryLearning(n_components=n_components, 
                                                  batch_size=batch_size, 
                                                  n_iter=1000, 
                                                  random_state=0)

# Fit the model to data X
dictionary_learning.fit(X)

# Transform the data into its sparse component representation
X_transformed = dictionary_learning.transform(X)

# Obtain dictionary of components
dictionary = dictionary_learning.components_

print("Sparse code:\n", X_transformed)
print("Dictionary components:\n", dictionary)
