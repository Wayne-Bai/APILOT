import tensorflow as tf

def resize_quantized_images(images, size):
    return tf.raw_ops.ResizeQuantized(images=images, size=size)
