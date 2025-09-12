import tensorflow as tf

def quantize_then_dequantize(tensor):
    # Quantize the tensor
    quantized_tensor = tf.quantization.quantize(tensor, tf.reduce_min(tensor), tf.reduce_max(tensor), tf.quint8)

    # Dequantize the tensor
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, tf.reduce_min(tensor), tf.reduce_max(tensor))

    return dequantized_tensor
