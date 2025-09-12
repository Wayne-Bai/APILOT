
import tensorflow as tf

def quantize_dequantize(input_tensor, num_bits=8):
    # Quantize the input tensor using tf.round
    quantized = tf.round(input_tensor * (2**num_bits - 1)) / (2**num_bits - 1)
    
    # Dequantize the quantized tensor using tf.bitwise.bitwise_xor and tf.math.bitwise_and
    dequantized = tf.bitwise.bitwise_xor(tf.bitwise.bitwise_and(quantized, 2**num_bits-1), 2**num_bits-1)
    
    return dequantized
