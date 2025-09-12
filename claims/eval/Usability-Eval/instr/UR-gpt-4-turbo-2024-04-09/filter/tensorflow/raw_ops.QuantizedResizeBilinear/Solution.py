import tensorflow as tf

def resize_quantized_images(images, size):
    """Resizes quantized images using bilinear interpolation without deprecated APIs.

    Args:
    images (tf.Tensor): A 4-D Tensor of shape `[batch, height, width, channels]` and dtype tf.uint8.
    size (Tuple[int, int]): A tuple of two integers, (new_height, new_width) specifying the new size.

    Returns:
    tf.Tensor: A 4-D tensor containing the resized images.
    """
    # Convert images from uint8 to float32
    float_images = tf.cast(images, tf.float32)

    # Resize images using bilinear interpolation
    resized_images = tf.image.resize(float_images, size, method='bilinear')

    # Convert images back to uint8
    output_images = tf.cast(resized_images, tf.uint8)

    return output_images

# Example of using the function
# Create a batch of images (e.g., 10 images of size 256x256 with 3 color channels, dtype uint8)
input_images = tf.random.uniform([10, 256, 256, 3], maxval=256, dtype=tf.uint8)

# Target new size
new_size = (128, 128)

# Resize the quantized images
output_images = resize_quantized_images(input_images, new_size)
