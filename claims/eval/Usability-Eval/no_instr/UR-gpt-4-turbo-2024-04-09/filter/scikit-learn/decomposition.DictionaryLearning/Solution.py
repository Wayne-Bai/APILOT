from sklearn.decomposition import DictionaryLearning
import numpy as np

# Example data: rows are samples and columns are features
X = np.random.rand(100, 50)  # 100 samples, 50 features

# Initialize the DictionaryLearning model
dict_learner = DictionaryLearning(n_components=10,  # number of basis/dictionary elements
                                  max_iter=500,
                                  transform_algorithm='lasso_lars',
                                  random_state=42)

# Fit the model to the data
dictionary = dict_learner.fit(X)

# Transform data into the sparse code using the learned dictionary
X_transformed = dict_learner.transform(X)

# Now `dictionary.components_` holds the basis components (the atoms)
print("Learned Dictionary:")
print(dictionary.components_)

print("Sparse Code:")
print(X_transformed)
