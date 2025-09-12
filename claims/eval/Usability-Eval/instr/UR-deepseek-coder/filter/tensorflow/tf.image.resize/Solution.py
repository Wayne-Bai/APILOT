import tensorflow as tf

def resize_images(images, target_size, method=tf.image.ResizeMethod.BILINEAR):
    """
    Resize images to the specified target size using the specified method.

    Args:
        images: A 4D tensor of shape [batch, height, width, channels].
        target_size: A tuple (new_height, new_width) specifying the target size.
        method: A tf.image.ResizeMethod specifying the resizing method.

    Returns:
        A 4D tensor of shape [batch, new_height, new_width, channels].
    """
    resized_images = tf.image.resize(images, target_size, method=method)
    return resized_images

# Example usage:
# images = ...  # Your 4D tensor of images
# target_size = (224, 224)
# resized_images = resize_images(images, target_size)
