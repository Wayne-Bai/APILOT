from sklearn.decomposition import MiniBatchSparsePCA

# Assuming X is your data
dictionary = MiniBatchSparsePCA(n_components=100, alpha=0.1, batch_size=500).fit_transform(X)
