import tensorflow as tf

def quantize_and_dequantize(input_tensor):
    # Quantize the input tensor
    quantized_tensor = tf.quantization.quantize(input_tensor, 0, 255, tf.quint8)

    # Dequantize the quantized tensor
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, 0, 255, tf.quint8)

    return dequantized_tensor

# Usage example:
input_tensor = tf.constant([1.1, 2.2, 3.3, 4.4, 5.5], dtype=tf.float32)
quantized_and_dequantized_tensor = quantize_and_dequantize(input_tensor)
print(quantized_and_dequantized_tensor)
