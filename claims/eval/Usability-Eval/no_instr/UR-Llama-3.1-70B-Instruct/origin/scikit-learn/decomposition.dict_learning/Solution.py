# Importing necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample signal
np.random.seed(0)
n_samples, n_features = 100, 10
y = np.random.randn(n_samples, n_features)

# Create a DictionaryLearning object with 10 components
dico = MiniBatchDictionaryLearning(n_components=10, alpha=1, n_iter=500)

# Fit the DictionaryLearning object to the signal
dico.fit(y)

# Get the dictionary (components_) and the sparse representation (transform())
components_ = dico.components_
transform_ = dico.transform(y)

# Plot the signal and the learned components
plt.figure(figsize=(10, 10))
for i, component in enumerate(components_):
    plt.subplot(5, 2, i + 1)
    plt.imshow(component.reshape((2, 5)), cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.title('Component %d' % (i + 1))
plt.show()

# Plot the original signal and the reconstructed signal
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(y.reshape((10, 10)), cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Original signal')
plt.subplot(1, 2, 2)
plt.imshow((dico.inverse_transform(transform_)).reshape((10, 10)), cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Reconstructed signal')
plt.show()
