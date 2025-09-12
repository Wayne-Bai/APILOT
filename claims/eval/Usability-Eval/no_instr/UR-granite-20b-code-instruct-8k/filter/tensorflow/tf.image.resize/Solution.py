import tensorflow as tf

def resize_images(images, size, method):
    """
    Resize images to size using the specified method.

    Args:
    images: A tensor of shape [batch, height_in, width_in, channels]
    size: A 1-D int32 Tensor of 2 elements: new_height, new_width.  The
    new size for the images.
    method: ResizeMethod.  must be one of ResizeMethod.NEAREST_NEIGHBOR,
    ResizeMethod.BILINEAR, or ResizeMethod.AREA.

    Returns:
    A tensor of shape [batch, height_out, width_out, channels]
    """
    return tf.image.resize(images, size, method)
