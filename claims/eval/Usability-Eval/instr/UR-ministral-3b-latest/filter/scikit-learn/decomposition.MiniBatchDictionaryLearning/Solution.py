from sklearn.dictionary_learning import MiniBatchDictionaryLearning
from sklearn.decomposition import TruncatedSVD

# Assuming you have your data ready, this could be a dataset in a matrix form
# X is your dataset
# from sklearn.metrics import mean_squared_error

# First, initialize the MiniBatchDictionaryLearning model
model = MiniBatchDictionaryLearning(n_components=50, solver='lars')

# Fit the model
model.fit(X)

# Get the learned dictionary
dictionary = model.components_

# You can also use TruncatedSVD for dimensionality reduction
# This can be helpful for visualization or further analysis
svd = TruncatedSVD(n_components=10)
X_transformed = svd.fit_transform(X)

print("Dictionary (mini-batch learned):")
print(dictionary)

print("\nTransformed dataset:")
print(X_transformed)
