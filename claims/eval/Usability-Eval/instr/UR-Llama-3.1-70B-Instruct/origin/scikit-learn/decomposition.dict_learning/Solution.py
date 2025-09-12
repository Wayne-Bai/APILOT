# Import necessary libraries
from sklearn.decomposition import DictionaryLearning
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load a dataset. Here, Iris dataset is used for demonstration purposes
iris = load_iris()
X = iris.data

# Initialize the dictionary learning object with 3 components (i.e., features)
dl = DictionaryLearning(n_components=3, max_iter=1000, random_state=0)

# Fit the model to the data
X_dl = dl.fit_transform(X)

# Components of the dictionary
components = dl.components_

# Transformed data (based on the learned dictionary)
transformed_data = X_dl

# Transform some rows of the original data to show the transformation
rows_to_transform = np.arange(10)
transformed_rows = dl.inverse_transform(X_dl[rows_to_transform])

# Verify that the transformation is consistent (though not exactly equal due to sparsity constraint)
print("Transformation Verification:")
print(np.allclose(X[rows_to_transform], transformed_rows))

# Print results
print("Components of the Dictionary:")
print(components)
print("Transformed Data Shape:")
print(transformed_data.shape)

# Show the original and reconstructed data through the learned dictionary
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Data")
plt.scatter(X[:, 0], X[:, 1])

plt.subplot(1,2,2)
plt.title("Transformed Data")
plt.scatter(X_dl[:, 0], X_dl[:, 1])
plt.tight_layout()
plt.show()
