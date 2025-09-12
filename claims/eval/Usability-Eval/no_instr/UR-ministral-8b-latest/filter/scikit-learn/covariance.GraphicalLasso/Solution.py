import numpy as np
from sklearn.covariance import LedoitWolf
from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

# Example usage

# Generate some sample data
np.random.seed(42)
n_samples = 100
n_features = 20
X = np.random.randn(n_samples, n_features)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Estimate the sparse inverse covariance matrix using Ledoit-Wolf
estimator = LedoitWolf()
estimator.fit(X_scaled)
inverse_covariance = estimator.inverse_covariance_

print("Sparse inverse covariance matrix:\n", inverse_covariance)

# Optionally, you can use Gaussian Mixture Models to learn the underlying distribution
gmm = GaussianMixture(n_components=n_features, random_state=42)
gmm.fit(X_scaled.reshape(-1, n_features))
log_likelihood = gmm.score_samples(X_scaled.reshape(-1, n_features))

print("Log likelihood of the GMM model:", log_likelihood)
