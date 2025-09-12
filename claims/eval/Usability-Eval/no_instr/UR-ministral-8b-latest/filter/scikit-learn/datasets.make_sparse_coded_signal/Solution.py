import numpy as np
from sklearn.decomposition import SparseComponentAnalysis

# Generate random data
X = np.random.rand(100, 5)  # 100 samples, 5 features

# Perform Sparse Component Analysis
sca = SparseComponentAnalysis(n_components=3)
sca.fit(X)
signals = sca.transform(X)
print(signals)
