from sklearn.covariance import SparseInverseCovariance
import numpy as np

# Generate some random data
np.random.seed(0)
n_samples = 50
n_features = 20
data = np.dot(np.random.randn(n_samples, n_features), np.random.randn(n_features, 2))

# Fit the SparseInverseCovariance model to the data
PIC = SparseInverseCovariance()
PIC.fit(data)

# Print the precision matrix
print(PIC.precision_)
