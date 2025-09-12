from sklearn.datasets import make_sparse_coded_signal
X, dictionary = make_sparse_coded_signal(n_samples=1, n_components=10, n_features=2000,
 n_nonzero_coefs=100, random_state=42)
print(X.density)
print(dictionary)
