import numpy as np
from sklearn.decomposition import NMF

# Sample data initialization
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# NMF
nmf = NMF(n_components=2, init='random', random_state=0)
W = nmf.fit_transform(X)
H = nmf.components_

print("Matrix W (X * H^):")
print(W)
print("Matrix H (W * X):")
print(H)
