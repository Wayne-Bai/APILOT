import sklearn
from sklearn.decomposition import DictionaryLearning
from sklearn.datasets import load_iris

# Load iris dataset
X = load_iris().data

# Perform mini-batch dictionary learning
dictionary = DictionaryLearning(n_components=2, n_jobs=-1)
dictionary.fit(X)

print(dictionary.components_)
