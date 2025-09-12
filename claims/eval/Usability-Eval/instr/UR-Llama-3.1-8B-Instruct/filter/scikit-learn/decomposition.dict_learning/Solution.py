# Import necessary libraries
from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.feature_extraction.image import UIImage
from skimage.data import coins
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (in this case, a sample image)
image = coins()
image = resize(image, (128, 128))  # Resize the image to a smaller size for faster computation

# Compute the supervision signal (i.e., perform some preprocessing)
image = image / 255.0
image = image.reshape(-1, 1)  # Reshape the image to be compatible with the dictionary learning algorithm

# Perform dictionary learning
dictionary_size = 16
n_pixels, n_samples = image.shape
dict = MiniBatchDictionaryLearning(n_components=dictionary_size, alpha=1, batch_size_batch=128, tol=0.0001, 
                                   max_iter=500, n_iter=10, verbose=False, tol_solver=0.0001, 
                                   l1_ratio_solver=0.01).fit(image).components_

# Display the learned dictionary
plt.figure(figsize=(5, 5))
for i in range(dict.shape[1]):
    plt.subplot(4, 4, i + 1)
    plt.imshow(dictionary_size * dict[:, i] - 0.5)
    plt.axis('off')
plt.show()

# Use the learned dictionary for matrix factorization
transformed_data = MiniBatchDictionaryLearning(n_components=dictionary_size, alpha=1, batch_size_batch=128, 
                                               tol=0.0001, max_iter=500, n_iter=10, verbose=False, 
                                               tol_solver=0.0001, l1_ratio_solver=0.01).fit_transform(image)

# Display the transformed data (i.e., the coefficients of matrix factorization)
plt.figure(figsize=(5, 5))
plt.imshow(np.concatenate([np.squeeze(transformed_data[:, i]) for i in range(transformed_data.shape[1])], axis=1).reshape(-1, 32))
plt.show()
