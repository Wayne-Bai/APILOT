import tensorflow as tf

def resize_images(images, target_size, method='bilinear'):
    # Convert method string to TensorFlow resize method
    if method == 'bilinear':
        resize_method = tf.image.ResizeMethod.BILINEAR
    elif method == 'nearest':
        resize_method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bicubic':
        resize_method = tf.image.ResizeMethod.BICUBIC
    elif method == 'area':
        resize_method = tf.image.ResizeMethod.AREA
    else:
        raise ValueError("Unsupported resize method: {}".format(method))

    # Resize the images
    resized_images = tf.image.resize(images, target_size, method=resize_method)
    return resized_images

# Example usage:
# images = ...  # Tensor of shape [batch_size, height, width, channels]
# target_size = (new_height, new_width)
# resized_images = resize_images(images, target_size, method='bilinear')
