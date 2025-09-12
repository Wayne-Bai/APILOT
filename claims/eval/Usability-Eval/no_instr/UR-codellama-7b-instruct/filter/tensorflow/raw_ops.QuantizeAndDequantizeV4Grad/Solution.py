
import tensorflow as tf

def quantize_and_dequantize_v4(x, scale):
    """
    Returns the gradient of QuantizeAndDequantizeV4.
    """
    return tf.raw_ops.QuantizeAndDequantizeV4(x=x, scale=scale)
