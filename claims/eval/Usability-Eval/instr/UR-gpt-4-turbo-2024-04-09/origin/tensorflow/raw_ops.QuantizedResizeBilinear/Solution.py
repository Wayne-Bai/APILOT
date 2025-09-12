import tensorflow as tf

def resize_quantized_images(images, size):
    """
    Resize quantized images using bilinear interpolation.

    Args:
    images (tf.Tensor): A Quantized tensor of shape (batch, height, width, channels).
    size (tuple of int): A tuple of two integers, new height and new width to which
                         the images tensor will be resized.

    Returns:
    tf.Tensor: Resized image tensor.
    """
    # Convert quantized images to float32 for resizing
    images_float = tf.cast(images, tf.float32)
    
    # Resize images using bilinear interpolation
    resized_images = tf.image.resize(images_float, size, method='bilinear')
    
    # Convert back the resized images to original dtype of the input
    resized_images_quantized = tf.cast(resized_images, images.dtype)

    return resized_images_quantized

# Example
input_image_quantized = tf.random.uniform([1, 224, 224, 3], dtype=tf.uint8)
new_size = (128, 128)
resized_image = resize_quantized_images(input_image_quantized, new_size)
print(resized_image.shape)
