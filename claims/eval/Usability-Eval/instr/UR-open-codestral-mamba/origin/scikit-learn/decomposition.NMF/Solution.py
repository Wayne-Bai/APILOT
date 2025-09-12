from sklearn.decomposition import NMF

# Assuming we have a non-negative matrix X
# we will initialize it with random numbers for this example
X = np.random.rand(10, 10)

# Initialize the NMF model
model = NMF(n_components=2)

# Fit the NMF model with the data
W = model.fit_transform(X)

# Get the learned components (H)
H = model.components_

print("W shape:", W.shape)
print("H shape:", H.shape)
