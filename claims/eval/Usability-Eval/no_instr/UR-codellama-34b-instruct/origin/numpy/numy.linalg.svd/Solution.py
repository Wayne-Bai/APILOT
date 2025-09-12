import numpy as np

# Load the data into a numpy array
data = np.loadtxt('data.csv', delimiter=',')

# Perform SVD on the data
U, sigma, Vt = np.linalg.svd(data)

# Print the results
print(U)
print(sigma)
print(Vt)
