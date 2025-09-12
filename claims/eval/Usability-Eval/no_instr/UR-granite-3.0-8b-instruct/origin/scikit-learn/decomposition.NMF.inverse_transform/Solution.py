from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Assuming X is your data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)  # You can change the number of components as per your requirement
X_pca = pca.fit_transform(X_scaled)

# To transform data back to its original space
X_original = pca.inverse_transform(X_pca)
