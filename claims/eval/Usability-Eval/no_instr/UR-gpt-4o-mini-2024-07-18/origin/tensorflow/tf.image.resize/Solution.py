import tensorflow as tf

def resize_images(image, target_size, method='bilinear'):
    # Convert the method to a TensorFlow resizing method
    if method == 'nearest':
        resize_method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bilinear':
        resize_method = tf.image.ResizeMethod.BILINEAR
    elif method == 'bicubic':
        resize_method = tf.image.ResizeMethod.BICUBIC
    elif method == 'gaussian':
        resize_method = tf.image.ResizeMethod.GAUSSIAN
    elif method == 'mitchellcubic':
        resize_method = tf.image.ResizeMethod.MITCHELLCUBIC
    else:
        raise ValueError(f'Unsupported method: {method}')

    # Resize the image using the specified method
    resized_image = tf.image.resize(image, target_size, method=resize_method)
    
    return resized_image
