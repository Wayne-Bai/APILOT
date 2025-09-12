# Import necessary libraries
import tensorflow as tf

# Define a function to resize quantized images
def resize_quantized_images(images, size):
    """
    Resize quantized images to size using quantized bilinear interpolation.

    Args:
    images (tf.Tensor): A 4-D tensor of shape `[batch, height, width, channels]`.
    size (tf.Tensor): A 1-D tensor of shape `[2]` representing the target size.

    Returns:
    tf.Tensor: The resized images.
    """
    # Define the minimum and maximum values for quantization
    min_value = -128
    max_value = 127

    # Ensure the images are quantized (int8 data type)
    images = tf.cast(images, tf.int8)

    # Resize the images using quantized bilinear interpolation
    resized_images = tf.raw_ops.ResizeQuantizedImagesV2(
        images=images,
        min_values=min_value,
        max_values=max_value,
        size=size,
        align_corners=False
    )

    return resized_images

# Example usage:
if __name__ == "__main__":
    # Create a sample image tensor
    images = tf.random.randint(0, 256, shape=[1, 224, 224, 3])
    images = tf.cast(images, tf.int8)

    # Define the target size
    size = tf.constant([112, 112])

    # Resize the images
    resized_images = resize_quantized_images(images, size)

    # Print the shape of the resized images
    print(resized_images.shape)
