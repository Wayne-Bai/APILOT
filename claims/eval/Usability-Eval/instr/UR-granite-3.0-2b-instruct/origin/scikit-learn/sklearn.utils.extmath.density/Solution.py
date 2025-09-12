from sklearn.neighbors import KernelDensity
import numpy as np

# Assuming X is your sparse vector
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Create a KernelDensity object
kde = KernelDensity(kernel='gaussian', bandwidth=1.0)

# Fit the model to your data
kde.fit(X.reshape(-1, 1))

# Compute the density of the sparse vector
density = kde.score_samples(X.reshape(-1, 1))
