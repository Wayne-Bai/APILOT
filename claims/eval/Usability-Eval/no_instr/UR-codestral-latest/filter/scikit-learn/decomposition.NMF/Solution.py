from sklearn.decomposition import NMF
import numpy as np

# Assume X is your non-negative matrix
# X = np.array(...)

# Create an NMF model
model = NMF(n_components=2, init='random', random_state=0)

# Fit the model
W = model.fit_transform(X)

# H is the components_ attribute of model
H = model.components_

# Verify the approximation
X_approx = np.dot(W, H)
