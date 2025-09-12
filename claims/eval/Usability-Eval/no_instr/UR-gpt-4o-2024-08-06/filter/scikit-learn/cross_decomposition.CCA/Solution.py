import numpy as np
from sklearn.cross_decomposition import CCA

# Sample data
X = np.array([[0.0, 0.1, 0.2],
              [0.1, 0.2, 0.3],
              [0.2, 0.3, 0.4],
              [0.3, 0.4, 0.5]])
Y = np.array([[1.0, 0.0],
              [2.0, 0.1],
              [3.0, 0.2],
              [4.0, 0.3]])

# Create a Canonical Correlation Analysis (CCA) object
cca = CCA(n_components=2)

# Fit the CCA model
cca.fit(X, Y)

# Transform the data
X_c, Y_c = cca.transform(X, Y)

print("Transformed X:")
print(X_c)
print("Transformed Y:")
print(Y_c)

# Optional: Check the correlation between the transformed variables
correlations = np.corrcoef(X_c.T, Y_c.T)
print("Correlations between transformed variables:")
print(correlations)
