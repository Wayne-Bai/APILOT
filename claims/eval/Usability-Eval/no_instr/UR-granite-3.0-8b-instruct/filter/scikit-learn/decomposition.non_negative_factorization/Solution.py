from sklearn.decomposition import NMF

# Assuming X is your non-negative matrix
X = ...

# Initialize the NMF model
nmf = NMF(n_components=2, random_state=0)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_
