# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import array_to_img

# Define a function to resize an image using a specified method
def resize_image(image_path, new_size, method='bilinear'):
    """
    Resize an image to a specified size using a specified method.

    Args:
        image_path (str): The path to the image to resize.
        new_size (tuple): The new size of the image.
        method (str, optional): The method to use for resizing. Defaults to 'bilinear'.

    Returns:
        tf.keras.preprocessing.image.array_to_img: The resized image.
    """

    # Load the image from the specified path
    image = load_img(image_path)

    # Convert the image to a numpy array
    image_array = img_to_array(image)

    # Convert the numpy array to a tensor
    image_tensor = tf.convert_to_tensor(image_array)

    # Define the resizing method to use
    if method == 'nearest':
        interpolation = tf.nearest
    elif method == 'bilinear':
        interpolation = tf.bilinear
    elif method == 'bicubic':
        interpolation = tf.bicubic
    elif method == 'area':
        interpolation = tf.area
    else:
        raise ValueError("Invalid method. Choose from 'nearest', 'bilinear', 'bicubic', or 'area'.")

    # Resize the image tensor
    resized_image_tensor = tf.image.resize(image_tensor, new_size, method=interpolation)

    # Convert the resized tensor back to a numpy array
    resized_image_array = resized_image_tensor.numpy()

    # Convert the numpy array back to an image
    resized_image = array_to_img(resized_image_array)

    return resized_image


# Example usage
image_path = 'path_to_your_image.jpg'
new_size = (256, 256)  # Resized image size
resized_image = resize_image(image_path, new_size)

from tensorflow.keras.preprocessing.image import save_img
save_img('resized_image.jpg', resized_image)
