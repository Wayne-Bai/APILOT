# Importing the necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# Load the image
def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.cast(img, tf.float32)
    return img

# Resize the image
def resize_image(image, new_size):
    resized_image = tf.image.resize(image, new_size)
    return resized_image

# Save the resized image
def save_image(image, image_path):
    image = tf.clip_by_value(image, 0, 255)
    image = tf.cast(image, tf.uint8)
    tf.image.save_jpeg(image, image_path)

# Start with an example image
image_path = "path_to_your_image.jpg"  # replace with your image path

# Load the image
image = load_image(image_path)

# Define the new size
new_size = (224, 224)  # replace with your desired size

# Resize the image using bilinear interpolation
resized_image = resize_image(image, new_size)

# Print the shape of the resized image
print(resized_image.shape)

# Save the resized image
save_image(resized_image, "resized_image.jpg")

# Display the original and resized images
original_image = tf.io.read_file(image_path)
original_image = tf.image.decode_image(original_image, channels=3)
original_image = tf.cast(original_image, tf.float32)

fig, axs = plt.subplots(1, 2, figsize=(15, 7))
axs[0].imshow(tf.cast(original_image, tf.uint8))
axs[0].set_title("Original Image")
axs[1].imshow(tf.cast(resized_image, tf.uint8))
axs[1].set_title("Resized Image")
plt.show()
