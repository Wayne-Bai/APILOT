import numpy as np
from sklearn.decomposition import NMF

# Create a dummy matrix X for demonstration
X = np.random.rand(10, 30)

# Dimensions of the latent space
n_factors = 10

# Perform Non-Negative Matrix Factorization
nmf = NMF(n_components=n_factors, random_state=42)
W = nmf.fit_transform(X)
H = nmf.components_

print("Matrix W:\n", W)
print("Matrix H:\n", H)
