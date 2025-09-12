import tensorflow as tf

def resize_image(image_path, size):
    """
    This function resizes an image to the specified size.

    Args:
    image_path: A string, the path to the image file.
    size: A tuple, a pair of a new width and height.

    Returns:
    resized_img: A tensor, the resized image.
    """
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, size)
    return img
