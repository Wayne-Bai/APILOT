import tensorflow as tf

def resize_q_image(image, size):
    """
    Resize quantized images to size using quantized bilinear interpolation.
    
    Args:
    image: A floating-point or non-float-type Tensor.
    size: An int or Tensor(shape=[2]), the new size for which to resize.
    
    Returns:
    A Tensor with the resize image.
    """
    
    # Convert the input image to a tf.uint8 type if it is not already.
    image = tf.cast(image, tf.uint8)
    
    # Check if the size tensor is provided with shape (2,).
    size_with_default = tf.cond(tf.shape(size)[0] == 2,
                                true_fn=lambda: size,
                                false_fn=lambda: tf.ones([2]))
    
    # Perform the resize using tf.raw_ops.ResizeBilinearQuantized.
    resized_image = tf.raw_ops.ResizeBilinearQuantized(
        input=image,
        size=size_with_default,
        align_corners=True,
        half_pixel_centers_from_hint=tf.int32(0)
    )
    
    return resized_image

# Example usage:
image = tf.random.uniform(shape=[256, 256, 3], minval=0, maxval=255, dtype=tf.uint8)
size = tf.constant((128, 128))
resized_image = resize_q_image(image, size)
