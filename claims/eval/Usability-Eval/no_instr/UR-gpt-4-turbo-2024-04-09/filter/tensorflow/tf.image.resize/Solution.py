import tensorflow as tf

def resize_image(image, target_height, target_width, method=tf.image.ResizeMethod.BILINEAR):
    """
    Resizes an image to a specified size using a specified method.

    :param image: Input tensor representing the image.
    :param target_height: Desired image height.
    :param target_width: Desired image width.
    :param method: Method of interpolation. One of `tf.image.ResizeMethod`, such as BILINEAR, NEAREST_NEIGHBOR,
                   BICUBIC, or LANCZOS3.
    :return: Resized image as a tensor.
    """
    resized_image = tf.image.resize(image, [target_height, target_width], method=method)
    return resized_image
