from sklearn.decomposition import NMF
import numpy as np

# Generate random data
X = np.random.rand(10, 5)

# Initialize NMF
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model
W = nmf.fit_transform(X)
H = nmf.components_

# Print the factors
print("Factor W:\n", W)
print("Factor H:\n", H)
