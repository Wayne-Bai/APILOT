import tensorflow as tf

def resize_image(image, size, method=tf.image.ResizeMethod.BILINEAR):
    # Convert image to tensorflow tensor if it is a numpy array
    if type(image).__module__ == 'numpy':
        image = tf.convert_to_tensor(image)
    # Resize image
    resized_image = tf.image.resize(image, size, method=method)
    return resized_image
