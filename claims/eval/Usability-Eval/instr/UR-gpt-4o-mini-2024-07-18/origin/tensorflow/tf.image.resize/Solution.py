import tensorflow as tf

def resize_images(image_tensor, target_size, method='bilinear'):
    """Resize images to the target size using the specified method."""
    if method == 'nearest':
        resized_images = tf.image.resize(image_tensor, target_size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    elif method == 'bilinear':
        resized_images = tf.image.resize(image_tensor, target_size, method=tf.image.ResizeMethod.BILINEAR)
    elif method == 'bicubic':
        resized_images = tf.image.resize(image_tensor, target_size, method=tf.image.ResizeMethod.BICUBIC)
    elif method == 'area':
        resized_images = tf.image.resize(image_tensor, target_size, method=tf.image.ResizeMethod.AREA)
    else:
        raise ValueError("Unsupported resize method: {}".format(method))
    
    return resized_images

# Example usage
# image_tensor = tf.random.uniform((1, 256, 256, 3))  # Example image tensor
# resized_image = resize_images(image_tensor, (128, 128), method='bilinear')
