import tensorflow as tf

# Method to resize an image
def resize_image(image_path, new_size, method=tf.image.ResizeMethod.BILINEAR):
    """
    Resizes an image to the specified size using the given method.

    Args:
    image_path (str): Path to the image file.
    new_size (tuple[int, int]): New size of the image as (height, width).
    method (tf.image.ResizeMethod): Method to use for resizing. Defaults to BILINEAR.

    Returns:
    tf.Tensor: Resized image.
    """
    # Read the image from file
    image_raw = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image_raw, channels=3)

    # Resize the image
    resized_image = tf.image.resize(image, new_size, method=method)

    # Ensure the resized image has the same data type as the original image
    resized_image = tf.cast(resized_image, image.dtype)

    return resized_image

# Example usage
image_path = 'path_to_your_image.jpg'
new_size = (256, 256)
resized_img = resize_image(image_path, new_size)

# Display the resized image
import matplotlib.pyplot as plt
plt.imshow(resized_img)
plt.axis('off')
plt.show()
