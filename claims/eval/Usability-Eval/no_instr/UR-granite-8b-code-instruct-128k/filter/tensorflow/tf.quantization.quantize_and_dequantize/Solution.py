import tensorflow as tf

# Quantize a tensor
def quantize(tensor):
    return tf.quantization.quantize(tensor)

# Dequantize a tensor
def dequantize(tensor):
    return tf.quantization.dequantize(tensor)
