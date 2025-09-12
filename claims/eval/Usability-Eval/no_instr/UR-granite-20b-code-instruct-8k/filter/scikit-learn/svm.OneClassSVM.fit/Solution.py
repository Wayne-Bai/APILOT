from sklearn.mixture import GaussianMixture

# Assuming X is your data
gmm = GaussianMixture(n_components=2, random_state=0).fit(X)
soft_boundary = gmm.predict_proba(X)
