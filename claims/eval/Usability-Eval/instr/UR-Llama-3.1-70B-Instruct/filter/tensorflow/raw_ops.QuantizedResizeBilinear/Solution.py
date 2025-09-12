import tensorflow as tf

def resize_quantized_images(images, size):
    """
    Resize quantized images to size using quantized bilinear interpolation.

    Args:
    images (tf.Tensor): A 4D tensor of shape [batch, height, width, channels].
    size (tf.Tensor): A 1D tensor of shape [2] containing the new height and width.

    Returns:
    tf.Tensor: A 4D tensor of shape [batch, new_height, new_width, channels] containing the resized images.
    """
    # Define the ResizeBilinear function from tf.raw_ops
    resize_bilinear = tf.raw_ops.ResizeBilinear

    # Calculate the new height and width
    new_height, new_width = size

    # Resize the images using quantized bilinear interpolation
    resized_images = resize_bilinear(
        images=images,
        size=[new_height, new_width]
    )

    return resized_images

# Example usage:
# Define a sample image tensor
image = tf.random.uniform(shape=[1, 256, 256, 3], dtype=tf.uint8)

# Define the new size
new_size = tf.constant([512, 512])

# Resize the image
resized_image = resize_quantized_images(image, new_size)

print(resized_image.shape)
