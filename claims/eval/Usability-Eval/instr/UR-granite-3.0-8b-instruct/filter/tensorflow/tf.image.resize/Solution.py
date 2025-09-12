import tensorflow as tf

def resize_images(images, size, method):
    return tf.image.resize(images, size, method)
