import tensorflow as tf

def resize_quantized_images(images, new_height, new_width):
    """
    Resizes quantized images to a specific size using quantized bilinear interpolation.

    Args:
    images: A 4-D Tensor containing quantized images values. The size of this tensor is [batch, in_height, in_width, in_channels].
    new_height: An int, the new height for the resized image.
    new_width: An int, the new width for the resized image.

    Returns:
    resized_images: A 4-D Tensor with the same type as images, containing the resized images with size [batch, new_height, new_width, in_channels].
    """
    with tf.compat.v1.Session() as sess:
        resized_images = tf.image.resize(images, [new_height, new_width], method=tf.image.ResizeMethod.BILINEAR)
        return sess.run(resized_images)

# Example usage
image = tf.random.uniform([1, 100, 100, 3], maxval=256, dtype=tf.int32)
resized_image = resize_quantized_images(image, 50, 50)
print(resized_image)
