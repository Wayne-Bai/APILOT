from sklearn.decomposition import NMF

# Assuming X is your non-negative matrix
# Replace 'X' with your actual matrix

# Initialize the NMF model
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_

print("Matrix W:")
print(W)
print("\nMatrix H:")
print(H)
