
import numpy as np
from sklearn.cross_decomposition import PLSRegression

# Generate some sample data
n_samples = 100
n_features = 5
X = np.random.rand(n_samples, n_features)
y = np.random.rand(n_samples)

# Fit the PLS model to the data
pls = PLSRegression(n_components=3)
pls.fit(X, y)

# Get the singular values and loadings
u = pls.x_scores_
v = pls.y_loadings_
sv = np.diag(np.dot(u.T, v))

# Print the results
print("Singular values:", sv)
print("Loadings:")
for i in range(len(pls.x_scores_)):
    print("  ", pls.x_loadings_[i])
