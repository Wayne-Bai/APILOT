from sklearn.decomposition import DictionaryLearning

# Assuming X is your data and n_components is the number of factors you want to extract
dl = DictionaryLearning(n_components=n_components, random_state=42)

# Fit the model on your data
dl.fit(X)

# Transform your data using the learned dictionary
X_transformed = dl.transform(X)
