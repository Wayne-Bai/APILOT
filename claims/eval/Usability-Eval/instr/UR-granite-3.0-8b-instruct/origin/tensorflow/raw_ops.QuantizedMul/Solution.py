import tensorflow as tf

def quantized_mul(x, y):
    x = tf.quantization.fake_quant_with_min_max_vars(x, min_value=0, max_value=255, narrow_range=True)
    y = tf.quantization.fake_quant_with_min_max_vars(y, min_value=0, max_value=255, narrow_range=True)
    return tf.raw_ops.QuantizedMul(x, y)
