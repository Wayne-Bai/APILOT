import tensorflow as tf

def resize_images(images, target_size, method):
    """
    Resize images to the specified target size using the specified method.

    Args:
    images: A 4D tensor of shape [batch, height, width, channels].
    target_size: A tuple (new_height, new_width) specifying the target size.
    method: A string specifying the resize method ('bilinear', 'nearest', 'bicubic', 'area').

    Returns:
    A 4D tensor of shape [batch, new_height, new_width, channels] containing the resized images.
    """
    methods = {
        'bilinear': tf.image.ResizeMethod.BILINEAR,
        'nearest': tf.image.ResizeMethod.NEAREST_NEIGHBOR,
        'bicubic': tf.image.ResizeMethod.BICUBIC,
        'area': tf.image.ResizeMethod.AREA
    }
    
    if method not in methods:
        raise ValueError(f"Unsupported resize method: {method}. Supported methods are: {list(methods.keys())}")
    
    resized_images = tf.image.resize(images, target_size, method=methods[method])
    return resized_images

# Example usage:
# resized_images = resize_images(images, (224, 224), 'bilinear')
