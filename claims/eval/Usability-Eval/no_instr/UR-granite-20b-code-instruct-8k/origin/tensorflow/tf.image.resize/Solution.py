import tensorflow as tf

def resize_image(image, size, method):
    """
    Resize an image to the specified size using the specified method.

    Args:
        image: The input image to resize.
        size: The desired size of the output image.
        method: The resizing method to use. Can be one of 'nearest', 'bilinear', or 'area'.

    Returns:
        The resized image.
    """
    if method not in ['nearest', 'bilinear', 'area']:
        raise ValueError("Invalid resizing method. Must be one of 'nearest', 'bilinear', or 'area'.")
    if method == 'nearest':
        method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bilinear':
        method = tf.image.ResizeMethod.BILINEAR
    elif method == 'area':
        method = tf.image.ResizeMethod.AREA

    return tf.image.resize(image, size, method=method)
