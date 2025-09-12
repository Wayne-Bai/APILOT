import tensorflow as tf

def resize_quantized_images(images, size, method):
    return tf.raw_ops.ResizeQuantizedImages(images=images, size=size, method=method)
