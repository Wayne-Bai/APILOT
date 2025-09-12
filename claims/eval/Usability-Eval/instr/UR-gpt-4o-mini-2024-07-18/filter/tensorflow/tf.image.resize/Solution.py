import tensorflow as tf

def resize_image(image, target_size, method='bilinear'):
    # Load the image
    image = tf.image.decode_image(image)
    
    # Resize the image
    if method == 'bilinear':
        resized_image = tf.image.resize(image, target_size, method=tf.image.ResizeMethod.BILINEAR)
    elif method == 'nearest':
        resized_image = tf.image.resize(image, target_size, method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    elif method == 'bicubic':
        resized_image = tf.image.resize(image, target_size, method=tf.image.ResizeMethod.BICUBIC)
    else:
        raise ValueError("Invalid resize method. Choose 'bilinear', 'nearest', or 'bicubic'.")
    
    return resized_image

# Example usage
# image_data = ...  # Load your image data as bytes or a tensor
# target_size = [height, width]
# resized = resize_image(image_data, target_size)
