import tensorflow as tf

def resize_image(image, size, method):
    resized_image = tf.image.resize(image, size, method=method)
    return resized_image
