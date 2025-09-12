from sklearn.decomposition import DictionaryLearning
import numpy as np

# Generate synthetic data
np.random.seed(0)
data = np.random.rand(100, 20)  # 100 samples, 20 features

# Initialize and fit the Dictionary Learning model
dl = DictionaryLearning(n_components=10, transform_algorithm='lasso')
dictionary = dl.fit(data).components_

# Transform the data using the learned dictionary
transformed_data = dl.transform(data)

print("Learned Dictionary:")
print(dictionary)
print("Transformed Data:")
print(transformed_data)
