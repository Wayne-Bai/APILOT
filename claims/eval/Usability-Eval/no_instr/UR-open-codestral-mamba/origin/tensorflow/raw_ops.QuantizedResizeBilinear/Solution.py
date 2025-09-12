import tensorflow as tf

def resize_quantized_image(image, size):
    return tf.image.resize(image, size, method=tf.image.ResizeMethod.BILINEAR)

