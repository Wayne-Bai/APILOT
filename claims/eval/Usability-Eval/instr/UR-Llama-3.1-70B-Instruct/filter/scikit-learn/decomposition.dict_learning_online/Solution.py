from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np

# Generate a random data matrix
np.random.seed(0)
X = np.random.rand(1000, 30)

# Online dictionary learning
dico = MiniBatchDictionaryLearning(n_components=10, alpha=1, n_iter=100, batch_size=3, random_state=0)

# Fit the data matrix
dico.fit(X)

# Get the decomposed data
transformed_data = dico.transform(X)
components = dico.components_

# Print the results
print("Shape of transformed data:", transformed_data.shape)
print("Shape of dictionary components:", components.shape)
print("Transformed data:\n", transformed_data)
print("Dictionary components:\n", components)
