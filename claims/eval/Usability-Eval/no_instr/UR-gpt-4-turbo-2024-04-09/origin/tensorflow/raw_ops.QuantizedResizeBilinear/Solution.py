import tensorflow as tf

def resize_quantized_images(images, new_size):
    """
    Resize quantized images using bilinear interpolation.

    Parameters:
        images (tf.Tensor): A batch of images in quantized format.
        new_size (tuple): The new size (height, width) to resize the images to.

    Returns:
        tf.Tensor: Resized images.
    """
    # Convert quantized images to float32 to use 'resize_images'
    images_float = tf.cast(images, tf.float32)

    # Resize images using bilinear interpolation
    resized_images = tf.image.resize(images_float, new_size, method='bilinear')

    # Quantize the images back to the original datatype
    resized_images_quantized = tf.saturate_cast(resized_images, images.dtype)

    return resized_images_quantized

# Example to use the function
# Create a dummy quantized image tensor
quantized_images = tf.random.uniform([1, 64, 64, 3], maxval=256, dtype=tf.uint8)
new_size = (128, 128)

# Resize quantized images
resized_quantized_images = resize_quantized_images(quantized_images, new_size)
print(resized_quantized_images.shape)
