# Import necessary libraries
import numpy as np
from sklearn.covariance import GraphicalLassoCV
import matplotlib.pyplot as plt
from sklearn.datasets import make_sparse_spd_matrix

# Generate a sample dataset
n_samples = 200
n_features = 20
prec = make_sparse_spd_matrix(n_features, alpha=.98, smallest_coef=.4, 
                             largest_coef=.7, connected=True)

# Generate data from the above precision matrix
X = np.random.multivariate_normal(mean=[0] * n_features, cov=np.linalg.inv(prec), 
                                  size=n_samples)

# Create an instance of the GraphicalLassoCV class
gl_cv = GraphicalLassoCV(alphas=5)

# Fit the model to the data
gl_cv.fit(X)

# Get the estimated covariance matrix 
cov_ = gl_cv.covariance_

# Get the estimated precision matrix (inverse covariance matrix)
prec_ = gl_cv.precision_

# Plot the output
plt.figure(figsize=(10, 8))
plt.subplot(121)
plt.imshow(cov_, cmap='RdBu_r')
plt.colorbar()
plt.title('Estimated covariance matrix')
plt.subplot(122)
plt.imshow(prec_, cmap='RdBu_r')
plt.colorbar()
plt.title('Estimated precision matrix')
plt.show()
