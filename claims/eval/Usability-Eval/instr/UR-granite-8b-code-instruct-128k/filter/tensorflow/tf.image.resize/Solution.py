
import tensorflow as tf

def resize_images(image, size, method=tf.image.ResizeMethod.BILINEAR):
    """
    Resize an image to the specified size using the specified method.

    Args:
        image: A 3-D tensor of shape [height, width, channels] representing the image.
        size: A 1-D tensor of shape [2] representing the new size of the image.
        method: The method to use for resizing, either tf.image.ResizeMethod.BILINEAR or tf.image.ResizeMethod.NEAREST_NEIGHBOR.

    Returns:
        A 3-D tensor of shape [size[0], size[1], channels] representing the resized image.
    """
    return tf.image.resize(image, size, method)
