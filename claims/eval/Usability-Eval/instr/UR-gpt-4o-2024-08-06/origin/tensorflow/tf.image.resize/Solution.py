import tensorflow as tf

def resize_image(image_path, target_size, method=tf.image.ResizeMethod.BILINEAR):
    """
    Resizes the image at the given path to the specified target size using the specified method.

    :param image_path: Path to the image file.
    :param target_size: Tuple of (height, width) specifying the desired output size.
    :param method: The method to use for resizing. Defaults to BILINEAR.
    :return: A tensor representing the resized image.
    """
    # Read the image file
    image = tf.io.read_file(image_path)
    # Decode the image
    image = tf.image.decode_image(image, channels=3)
    # Resize the image
    resized_image = tf.image.resize(image, target_size, method=method)
    return resized_image

# Example usage
image_path = "path/to/your/image.jpg"
target_size = (256, 256)  # Example target size

resized_image = resize_image(image_path, target_size)

# If you need to visualize or save the resulting image, convert it to a format that can be used
# For example, converting to a uint8 tensor suitable for saving:
resized_image_uint8 = tf.image.convert_image_dtype(resized_image, dtype=tf.uint8)

# Save or do other operations with the resized_image_uint8 as needed
print(resized_image_uint8.shape)
