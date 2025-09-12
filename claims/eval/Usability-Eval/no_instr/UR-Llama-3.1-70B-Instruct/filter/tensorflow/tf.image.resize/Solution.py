# Import necessary libraries
import tensorflow as tf
import numpy as np

# Function to resize image to specified size using specified method
def resize_image(image, size, method):
    """
    Resize image to specified size using specified method.

    Args:
        image (tf.Tensor): Image tensor to resize.
        size (tuple): Target size (height, width).
        method (str): Resizing method. Options: 'bilinear', 'nearest', 'bicubic', 'lanczos3', 'lanczos5', 'gaussian', 'area'.

    Returns:
        tf.Tensor: Resized image tensor.
    """
    # Use tf.image.resize method with specified resizing method
    if method == 'bilinear':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.BILINEAR)
    elif method == 'nearest':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    elif method == 'bicubic':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.BICUBIC)
    elif method == 'lanczos3':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.LANCZOS3)
    elif method == 'lanczos5':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.LANCZOS5)
    elif method == 'gaussian':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.GAUSSIAN)
    elif method == 'area':
        resized_image = tf.image.resize(image, size, method=tf.image.ResizeMethod.AREA)
    else:
        raise ValueError('Invalid resizing method')

    return resized_image

# Example usage
if __name__ == "__main__":
    # Create a sample image tensor
    image = tf.random.normal((256, 256, 3))

    # Resize the image to 512x512 using bilinear method
    resized_image = resize_image(image, (512, 512), 'bilinear')

    print(resized_image.shape)  # Output: (512, 512, 3)
