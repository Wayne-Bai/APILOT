# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Create a function to resize images
def resize_images(image, size, method):
    # Resize images using the specified method
    if method == 'nearest':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    elif method == 'bilinear':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.BILINEAR)
    elif method == 'bicubic':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.BICUBIC)
    elif method == 'area':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.AREA)
    elif method == 'lanczos3':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.LANCZOS3)
    elif method == 'lanczos5':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.GAUSSIAN)
    else:
        raise ValueError('Invalid resize method')

    return resized_image

# Load an image
image_path = 'path_to_your_image.jpg'
raw_image = keras.preprocessing.image.load_img(image_path)
image = keras.preprocessing.image.img_to_array(raw_image)

# Resize the image
resized_image = resize_images(image, (256, 256), 'bilinear')

# Display the original and resized images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(tf.keras.preprocessing.image.array_to_img(image))
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(tf.keras.preprocessing.image.array_to_img(resized_image))
plt.title('Resized Image')
plt.show()
