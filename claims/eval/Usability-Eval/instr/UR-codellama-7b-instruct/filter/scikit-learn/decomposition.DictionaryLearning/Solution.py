
from sklearn.decomposition import DictionaryLearning

# Set the hyperparameters for the Dictionary Learning algorithm
n_components = 100
alpha = 0.1
max_iterations = 1000

# Initialize the Dictionary Learning algorithm with the desired hyperparameters
dict_learner = DictionaryLearning(n_components=n_components, alpha=alpha, max_iterations=max_iterations)

# Fit the Dictionary Learning algorithm to the data
X_learned = dict_learner.fit(X)

# Print the resulting dictionary (atoms)
print(dict_learner.components_)
