from sklearn.decomposition import MiniBatchSparsePCA
import numpy as np

# Generate synthetic data
X = np.random.rand(100, 50)  # 100 samples, 50 features

# Configure MiniBatchSparsePCA
n_components = 10  # Number of dictionary elements
minibatch_size = 20  # Size of each minibatch

# Initialize the MiniBatchSparsePCA
model = MiniBatchSparsePCA(n_components=n_components, batch_size=minibatch_size, random_state=0)

# Fit the model on the data
model.fit(X)

# Transform the data
X_transformed = model.transform(X)

# Print the learned dictionary
dictionary = model.components_
print("Learned dictionary:")
print(dictionary)

# Print the transformed data
print("Transformed data:")
print(X_transformed)
