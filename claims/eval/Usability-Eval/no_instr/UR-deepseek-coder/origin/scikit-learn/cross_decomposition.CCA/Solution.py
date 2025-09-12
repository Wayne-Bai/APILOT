import numpy as np
from sklearn.cross_decomposition import CCA

# Example data
X = np.random.rand(100, 5)  # 100 samples, 5 features
Y = np.random.rand(100, 3)  # 100 samples, 3 features

# Initialize the CCA model
cca = CCA(n_components=2)  # You can set the number of components you want

# Fit the model
cca.fit(X, Y)

# Transform the data to the canonical components
X_c, Y_c = cca.transform(X, Y)

# Print the transformed data
print("Transformed X:", X_c)
print("Transformed Y:", Y_c)
