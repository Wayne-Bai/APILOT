import tensorflow as tf

def quantized_batch_normalization(inputs, scale, offset, mean, variance, min_input, max_input, epsilon=1e-5, num_bits=8, narrow_range=False):
    # Quantize the inputs
    quantized_inputs = tf.quantization.quantize(inputs, min_input, max_input, tf.qint8, mode='SCALED')
    
    # Perform batch normalization
    normalized_inputs = tf.nn.batch_normalization(tf.cast(quantized_inputs, tf.float32), mean, variance, offset, scale, epsilon)
    
    # Dequantize the normalized inputs
    dequantized_inputs = tf.quantization.dequantize(tf.cast(normalized_inputs, tf.qint8), min_input, max_input, mode='SCALED')
    
    return dequantized_inputs

# Example usage
# inputs = ... (your input tensor)
# scale = ... (your scale tensor)
# offset = ... (your offset tensor)
# mean = ... (your mean tensor)
# variance = ... (your variance tensor)
# min_input = ... (minimum value of the input tensor)
# max_input = ... (maximum value of the input tensor)

# normalized_output = quantized_batch_normalization(inputs, scale, offset, mean, variance, min_input, max_input)
