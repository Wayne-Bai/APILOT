
import tensorflow as tf

def resize_quantized_images(images, size):
    return tf.raw_ops.QuantizedResizeBilinear(images=images, size=size)
