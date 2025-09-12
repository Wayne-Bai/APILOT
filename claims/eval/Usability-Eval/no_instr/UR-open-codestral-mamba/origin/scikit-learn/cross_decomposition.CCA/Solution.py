# Importing the required libraries
from sklearn.cross_decomposition import CCA

# Generate some sample data
import numpy as np
X = np.random.rand(100, 5)
Y = np.random.rand(100, 3)

# Initialize CCA
cancor = CCA(n_components=1)

# Fit the model
cancor.fit(X, Y)

# Transform the data
X_transformed = cancor.transform(X)
Y_transformed = cancor.transform(Y)
