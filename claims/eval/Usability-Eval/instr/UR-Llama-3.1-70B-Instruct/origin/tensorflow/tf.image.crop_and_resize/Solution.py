import tensorflow as tf
from tensorflow import keras
import numpy as np

# Define a function that extracts crops from an image and resizes them
def crop_and_resize(images, box_ind, crop_size):
    """
    Extracts crops from an input image tensor and resizes them.

    Args:
    images (tf.Tensor): A tensor representing the input image.
    box_ind (tf.Tensor): A tensor representing the indices of the boxes.
    crop_size (int): The size of the crop.

    Returns:
    tf.Tensor: A tensor representing the resized crops.
    """
    # Extract crops from the input image
    crops = tf.image.extract_glimpse(images, [crop_size, crop_size], box_ind)
    
    # Resize the crops to a uniform size
    resized_crops = tf.image.resize(crops, (crop_size, crop_size), method="bilinear")

    return resized_crops

# Example usage:
image_data = np.random.randint(0, 255, (1, 256, 256, 3))
image_tensor = tf.convert_to_tensor(image_data, dtype=tf.float32)
box_ind = tf.constant([[10, 10]], dtype=tf.int32)
crop_size = 96
resized_crop = crop_and_resize(image_tensor, box_ind, crop_size)
print(resized_crop.shape)
