import tensorflow as tf
from tensorflow.python.ops import array_ops

def quantized_resize_bilinear(images, size):
    images = tf.cast(images, tf.float32)
    images = tf.raw_ops.QuantizedResizeBilinear(images=images, size=size, align_corners=False)
    images = array_ops.quantize_v2(images, min=0.0, max=255.0, Tout=tf.quint8)
    return images
