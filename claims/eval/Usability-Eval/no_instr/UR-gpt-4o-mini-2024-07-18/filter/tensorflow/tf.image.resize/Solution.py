import tensorflow as tf

def resize_image(image, target_size, method='bilinear'):
    # Convert method to appropriate TensorFlow resizing method
    if method == 'bilinear':
        method = tf.image.ResizeMethod.BILINEAR
    elif method == 'nearest':
        method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bicubic':
        method = tf.image.ResizeMethod.BICUBIC
    elif method == 'area':
        method = tf.image.ResizeMethod.AREA
    else:
        raise ValueError("Unsupported resizing method. Use 'bilinear', 'nearest', 'bicubic', or 'area'.")

    # Resize the image
    resized_image = tf.image.resize(image, target_size, method=method)
    return resized_image
