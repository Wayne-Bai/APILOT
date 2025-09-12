import sklearn
from sklearn.decomposition import NMF

# Load the data
X = ... # load the non-negative matrix X

# Initialize the model
nmf = NMF(n_components=2)

# Fit the model to the data
W, H = nmf.fit_transform(X)
