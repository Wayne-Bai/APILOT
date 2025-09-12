from sklearn.decomposition import NMF

# Assume X is your data matrix
# Initialize the NMF model
nmf = NMF(n_components=10, random_state=42)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_

# The learned dictionary is given by H
print("Learned dictionary:\n", H)
