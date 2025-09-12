import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import CanonicalCorrelationMatrix
from sklearn.cross_decomposition import SingularValueDecomposition

# Generating random data
np.random.seed(0)
X = np.random.rand(100, 5)
Y = np.random.rand(100, 5)

# Fit the CanonicalCorrelationMatrix
ccm = CanonicalCorrelationMatrix(n_components=2)
ccm.fit(X, Y)
U, V = ccm.uca, ccm.bca

# Scaling Projection
U_scaled = U / np.max(np.abs(U))
V_scaled = V / np.max(np.abs(V))

# Plotting the transformed data
min_val = np.min([np.min(U_scaled), np.min(V_scaled)])
max_val = np.max([np.max(U_scaled), np.max(V_scaled)])

fig, ax = plt.subplots()
ax.scatter(U_scaled[:, 0], U_scaled[:, 1], c='r', label='U data')
ax.scatter(V_scaled[:, 0], V_scaled[:, 1], c='b', label='V data')
ax.set_xlim(min_val, max_val)
ax.set_ylim(min_val, max_val)
ax.legend()
plt.show()
