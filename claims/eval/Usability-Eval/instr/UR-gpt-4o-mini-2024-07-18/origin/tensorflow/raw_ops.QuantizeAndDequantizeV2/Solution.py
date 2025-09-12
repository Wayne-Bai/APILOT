import tensorflow as tf

def quantize_dequantize_tensor(tensor):
    # Quantization
    quantized_tensor = tf.quantization.quantize(tensor, 
                                                  input_min=0.0, 
                                                  input_max=10.0, 
                                                  T=tf.qint8, 
                                                  mode='MIN_COMBINED')[0]
    
    # Dequantization
    dequantized_tensor = tf.quantization.dequantize(quantized_tensor, 
                                                     input_min=0.0, 
                                                     input_max=10.0)

    return dequantized_tensor

# Example usage
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
output_tensor = quantize_dequantize_tensor(input_tensor)
print(output_tensor)
