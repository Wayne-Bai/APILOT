
import tensorflow as tf

def resize_images(images, size, method='bilinear'):
    if method == 'bilinear':
        method = tf.image.ResizeMethod.BILINEAR
    elif method == 'nearest':
        method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bicubic':
        method = tf.image.ResizeMethod.BICUBIC
    elif method == 'area':
        method = tf.image.ResizeMethod.AREA
    else:
        raise ValueError("Invalid method. Please choose from 'bilinear', 'nearest', 'bicubic', or 'area'.")

    resized_images = tf.image.resize(images, size, method=method)

    return resized_images
