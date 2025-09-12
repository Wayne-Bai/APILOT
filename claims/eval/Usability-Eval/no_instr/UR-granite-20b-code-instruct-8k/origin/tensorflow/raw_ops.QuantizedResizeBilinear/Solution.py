import tensorflow as tf

def Resize_quantized_images_to_size(images, size, method):
    """Resize quantized images to size using quantized bilinear interpolation.

    Args:
        images: A `Tensor`. Must be one of the following types: `uint8`, `uint16`.
            N-D with shape `[batch, height, width, channels]`.
        size: A 1-D int32 `Tensor` of 2 elements: `new_height, new_width`.  The
            new size for the images.
        method: A `Tensor` of type `tf.float32`. Resize method to use.

    Returns:
        A `Tensor`. Has the same type as `images`.
    """
    return tf.raw_ops.ResizeQuantized(images=images, size=size, method=method)
