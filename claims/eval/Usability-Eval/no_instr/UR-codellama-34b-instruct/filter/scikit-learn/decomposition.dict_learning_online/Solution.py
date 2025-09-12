import numpy as np
from sklearn.decomposition import NMF

# Load the data
data = ...

# Initialize the model with the number of features and components
model = NMF(n_components=10)

# Fit the model to the data
W = model.fit_transform(data)

# Get the feature matrices
H = model.components_

# Print the results
print("Dictionary:")
print(np.round(H, 2))
print("Features:")
print(np.round(W, 2))
