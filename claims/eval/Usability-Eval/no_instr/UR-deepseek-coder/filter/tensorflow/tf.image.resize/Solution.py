import tensorflow as tf

def resize_images(images, target_size, method):
    # Convert the method string to the corresponding TensorFlow resize method
    if method == 'bilinear':
        resize_method = tf.image.ResizeMethod.BILINEAR
    elif method == 'nearest':
        resize_method = tf.image.ResizeMethod.NEAREST_NEIGHBOR
    elif method == 'bicubic':
        resize_method = tf.image.ResizeMethod.BICUBIC
    elif method == 'area':
        resize_method = tf.image.ResizeMethod.AREA
    else:
        raise ValueError("Unsupported resize method. Choose from 'bilinear', 'nearest', 'bicubic', 'area'.")

    # Resize the images
    resized_images = tf.image.resize(images, target_size, method=resize_method)
    return resized_images

# Example usage:
# images = ...  # Tensor of images with shape [batch, height, width, channels]
# target_size = (new_height, new_width)
# method = 'bilinear'  # or 'nearest', 'bicubic', 'area'
# resized_images = resize_images(images, target_size, method)
