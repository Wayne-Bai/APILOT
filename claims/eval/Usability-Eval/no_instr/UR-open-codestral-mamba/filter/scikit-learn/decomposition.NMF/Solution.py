# Importing required Scikit-learn library for NMF
from sklearn.decomposition import NMF

# Let's assume we have a non-negative matrix X
X = [
  [2, 1],
  [0, 2],
  [4, 0]
]

# We want to reduce this matrix to 2 dimensions for simplicity
# Creating an NMF object with 2 components
nmf = NMF(n_components=2)

# Fitting the NMF model to our data
nmf.fit(X)

# Getting the learned components/topics from the NMF model
W = nmf.components_

# Getting the matrix H (i.e. coefficient matrix)
H = nmf.transform(X)

print('Approximated matrix W: \n', W)
print('Coefficient matrix H: \n', H)
