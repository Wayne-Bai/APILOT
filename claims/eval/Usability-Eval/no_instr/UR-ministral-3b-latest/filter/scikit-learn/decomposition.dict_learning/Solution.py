import numpy as np
from sklearn.decomposition import NMF

# Example data
data = np.array([[50, 2, 32],
                 [234, 2, 100],
                 [101, 0, 100],
                 [1, 6, 100]])

# Define the model parameters
n_components = 2
alpha = 0.1
l1_ratio = 0.5
max_iter = 100

# Fit the model
model = NMF(n_components=n_components, init='random', alpha=alpha, losspolicy='multi-step').fit(data)

# Print the features (components) learned by the model
print("Features (Components):\n", model.components_)

# Print the coefficients (weights) learned by the model
print("Coefficients (Weights):\n", model.transform(data))
