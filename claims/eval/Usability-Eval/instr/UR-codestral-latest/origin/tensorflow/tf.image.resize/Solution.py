import tensorflow as tf

def resize_images(images, size, method=tf.image.ResizeMethod.BILINEAR):
    resized_images = tf.image.resize(images, size, method=method)
    return resized_images
