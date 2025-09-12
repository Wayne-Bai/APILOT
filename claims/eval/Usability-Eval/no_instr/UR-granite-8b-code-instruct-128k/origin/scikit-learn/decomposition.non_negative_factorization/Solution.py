from sklearn.decomposition import NMF
import numpy as np

# Assume X is your non-negative matrix
nmf = NMF(n_components=2)
W = nmf.fit_transform(X)
H = nmf.components_
