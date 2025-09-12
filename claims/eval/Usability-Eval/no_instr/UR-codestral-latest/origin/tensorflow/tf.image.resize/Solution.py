import tensorflow as tf

def resize_images(images, size, method=tf.image.ResizeMethod.BILINEAR):
    """
    This function resizes a batch of images to a specific size.

    :param images: A tensor of shape [batch, height, width, channels].
    :param size: A 1-D int32 Tensor of 2 elements: new_height, new_width.
    :param method: The resize method. Default is tf.image.ResizeMethod.BILINEAR.
    :return: A Tensor of type float32 containing the resized images.
    """
    resized_images = tf.image.resize(images, size, method=method)
    return resized_images
