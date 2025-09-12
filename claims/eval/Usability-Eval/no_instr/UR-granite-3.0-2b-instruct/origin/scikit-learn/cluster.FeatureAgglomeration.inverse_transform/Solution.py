from sklearn.decomposition import PCA

def inverse_transformation(X, n_components):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X)
    X_inverse = pca.inverse_transform(X_pca)
    return X_inverse
