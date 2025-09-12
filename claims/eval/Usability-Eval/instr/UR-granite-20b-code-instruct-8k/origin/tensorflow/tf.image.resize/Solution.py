
import tensorflow as tf

def resize_image(image, size, method='bilinear'):
    """
    Resize an image to the specified size using the specified method.

    Args:
        image: The image to resize.
        size: The desired size of the image (width, height).
        method: The resizing method to use ('bilinear', 'nearest', etc.).

    Returns:
        The resized image.
    """
    method = method.lower()
    if method == 'bilinear':
        return tf.image.resize(image, size, method=tf.image.ResizeMethod.BILINEAR)
    elif method == 'nearest':
        return tf.image.resize(image, size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    else:
        raise ValueError("Invalid resizing method: must be either 'bilinear' or 'nearest'.")
