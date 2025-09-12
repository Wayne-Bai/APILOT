import tensorflow as tf

def resize_images(images, size, method=tf.image.ResizeMethod.BILINEAR):
    return tf.image.resize(images, size, method)
