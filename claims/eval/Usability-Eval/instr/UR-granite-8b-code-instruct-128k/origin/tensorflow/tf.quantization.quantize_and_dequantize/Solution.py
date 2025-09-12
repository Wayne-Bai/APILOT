
import tensorflow as tf

# Quantizes then dequantizes a tensor.
def quantize_then_dequantize(tensor):
    quantized_tensor = tf.quantization.quantize(tensor, dtype=tf.quint8)
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, dtype=tf.float32)
    return dequantized_tensor
