from sklearn.linear_model import OrthogonalMatchingPursuit

# Initialize the ORMP model with the desired parameters
ormp = OrthogonalMatchingPursuit(n_nonzero_coefs=10)

# Fit the ORMP model to the data
ormp.fit(X)

# Generate a signal as a sparse combination of dictionary elements
signal = ormp.transform(X)
