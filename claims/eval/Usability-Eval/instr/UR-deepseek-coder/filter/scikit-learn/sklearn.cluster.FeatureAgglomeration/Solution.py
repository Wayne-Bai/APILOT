from sklearn.cluster import FeatureAgglomeration
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the iris dataset as an example
data = load_iris()
X = data.data

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize FeatureAgglomeration with desired number of clusters
agglo = FeatureAgglomeration(n_clusters=2)

# Fit and transform the data
X_reduced = agglo.fit_transform(X_scaled)

print(X_reduced)
