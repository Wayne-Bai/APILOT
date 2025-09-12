
from sklearn.decomposition import NMF

# Importing X as a numpy array
X = np.array([[1, 2], [3, 4], [5, 6]])

# Initializing the NMF algorithm with k=2
nmf = NMF(n_components=2)

# Fitting the NMF model to X
W, H = nmf.fit_transform(X)
