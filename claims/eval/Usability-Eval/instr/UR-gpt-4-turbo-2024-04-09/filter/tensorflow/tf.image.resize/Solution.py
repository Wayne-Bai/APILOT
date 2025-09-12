import tensorflow as tf

# Function to resize an image to the specified size using a specified method
def resize_image(image, target_height, target_width, method=tf.image.ResizeMethod.BILINEAR):
    resized_image = tf.image.resize(image, [target_height, target_width], method=method)
    return resized_image

# Example usage:
# Load an image (assuming you have a tensor 'image_tensor' of shape [height, width, channels])
# image_tensor = ...

# Resize the image to 300x300 using nearest neighbor method
# resized_image = resize_image(image_tensor, 300, 300, tf.image.ResizeMethod.NEAREST_NEIGHBOR)
