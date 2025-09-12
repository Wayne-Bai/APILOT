import tensorflow as tf

def resize_quantized_images(images, size):
    """
    Resize quantized images to a specified size using bilinear interpolation.

    :param images: A 4-D Tensor of shape [batch, height, width, channels] and type uint8.
    :param size: A list or tuple with two elements [new_height, new_width] specifying the new size.
    :return: A Tensor of the same type as `images`.
    """
    # Convert images from quantized uint8 to float32
    images_float = tf.cast(images, tf.float32)
    
    # Resize images using bilinear interpolation
    resized_images_float = tf.image.resize(images_float, size, method=tf.image.ResizeMethod.BILINEAR)
    
    # Quantize the images back to uint8
    resized_images_quantized = tf.cast(resized_images_float, tf.uint8)

    return resized_images_quantized

# Example usage:
# Assuming `quantized_images` is a uint8 tensor of shape [batch, height, width, channels]
# new_size = [new_height, new_width]
# resized_images = resize_quantized_images(quantized_images, new_size)
