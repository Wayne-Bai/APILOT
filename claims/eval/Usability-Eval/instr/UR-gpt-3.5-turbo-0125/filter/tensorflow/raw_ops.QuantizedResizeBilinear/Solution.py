
import tensorflow as tf

def resize_quantized_images(images, size):
    resized_images = tf.image.resize(images, size, method=tf.image.ResizeMethod.BILINEAR)
    return resized_images
