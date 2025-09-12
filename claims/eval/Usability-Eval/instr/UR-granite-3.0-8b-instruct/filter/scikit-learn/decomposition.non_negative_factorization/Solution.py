from sklearn.decomposition import NMF

# Assuming X is your non-negative matrix
X = ...  # replace with your matrix

# Initialize NMF with the desired number of components
nmf = NMF(n_components=2)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_
