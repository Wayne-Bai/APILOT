# Importing the scikit-learn library
from sklearn.decomposition import NMF

# Instantiating the NMF model
nmf_model = NMF(n_components=2, init='random', random_state=42)

# Assuming X is your non-negative matrix
W = nmf_model.fit_transform(X)
H = nmf_model.components_

print("W matrix (approximation of X): ")
print(W)

print("H matrix (factors of X): ")
print(H)
