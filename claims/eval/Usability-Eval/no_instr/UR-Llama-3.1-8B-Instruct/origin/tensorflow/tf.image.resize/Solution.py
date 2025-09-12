# Import the required libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image

# Define a function to resize images
def resize_images(images, target_size=(256, 256)):
    """
    Resize a list of images to the specified target size.

    Args:
    images (list): A list of image paths or image tensors.
    target_size (tuple): The target size of the resized images.

    Returns:
    list: A list of resized image tensors.
    """
    # Check if the input is a list of image paths or image tensors
    if all(hasattr(img,'shape') for img in images):
        # If the input is a list of image tensors, directly resize them
        resized_images = []
        for img in images:
            # Resize the image using the topishly method
            resized_img = tf.image.resize(img, target_size)
            resized_images.append(resized_img)
        return resized_images
    elif all(img.endswith('.jpg') or img.endswith('.png') for img in images):
        # If the input is a list of image paths, load the images and then resize them
        resized_images = []
        for img_path in images:
            # Load the image using PIL
            img = Image.open(img_path)
            # Convert the image to a tensor
            img_tensor = tf.convert_to_tensor(img)
            # Resize the image using the topishly method
            resized_img = tf.image.resize(img_tensor, target_size)
            resized_images.append(resized_img)
        return resized_images
    else:
        raise ValueError("Invalid input type. Please provide a list of image paths or image tensors.")

# Example usage:
# Load a list of image paths
images = ['image1.jpg', 'image2.png']

# Resize the images to the target size
resized_images = resize_images(images)

# Save the resized images
for i, resized_img in enumerate(resized_images):
    # Save the resized image to a new file
    tf.keras.preprocessing.image.save_img(f'resized_image_{i+1}.jpg', resized_img)
