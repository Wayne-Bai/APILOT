from sklearn.decomposition import NMF

# Assuming you have a non-negative matrix X
nmf = NMF(n_components=2)
W = nmf.fit_transform(X)
H = nmf.components_
