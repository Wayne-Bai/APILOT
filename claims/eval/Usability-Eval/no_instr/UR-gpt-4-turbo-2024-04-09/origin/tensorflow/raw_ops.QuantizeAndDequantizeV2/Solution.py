import tensorflow as tf

def quantize_dequantize_tensor(tensor, min_range, max_range):
    # Quantize the tensor
    quantized_tensor = tf.quantization.quantize(tensor, min_range, max_range, tf.qint8, mode='MIN_FIRST')[0]
    # Dequantize the tensor
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, min_range, max_range, tf.qint8, mode='MIN_FIRST')
    return dequantized_tensor

# Example usage
tensor = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)
min_range = 0.0
max_range = 4.0

result = quantize_dequantize_tensor(tensor, min_range, max_range)
print(result)
