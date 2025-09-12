import tensorflow as tf

def quantize_and_dequantize_tensor(tensor, num_bits=8, method='MIN_COMBINED'):
    # Quantize the input tensor
    scale, zero_point = tf.quantization.quantize(tensor, 
                                                  tf.reduce_min(tensor), 
                                                  tf.reduce_max(tensor), 
                                                  T=tf.int8, 
                                                  mode=method)

    # Dequantize the tensor back to the original range
    dequantized_tensor = tf.quantization.dequantize(scale, 
                                                     tf.cast(zero_point, tf.float32), 
                                                     tf.reduce_min(tensor), 
                                                     tf.reduce_max(tensor))
    return dequantized_tensor

# Example usage
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
output_tensor = quantize_and_dequantize_tensor(input_tensor)
print(output_tensor)
