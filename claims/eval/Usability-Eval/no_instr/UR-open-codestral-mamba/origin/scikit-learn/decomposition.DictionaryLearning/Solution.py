# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.feature_extraction.image import extract_patches_2d

# Load your dataset and store it in variable 'data'

# Transform the data into 2D patches
patch_size = (8, 8)
data = extract_patches_2d(data, patch_size)

# Initialize the MiniBatchDictionaryLearning object and fit the model
dictionary_learn = MiniBatchDictionaryLearning(n_components=100, random_state=0)
dictionary_learn.fit(data)

# Extract the learned dictionary from the model
dictionary = dictionary_learn.components_
