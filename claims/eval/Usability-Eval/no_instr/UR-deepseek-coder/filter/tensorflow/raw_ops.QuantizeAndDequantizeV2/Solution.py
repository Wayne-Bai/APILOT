import tensorflow as tf

def quantize_and_dequantize_tensor(input_tensor, input_min, input_max, num_bits=8, range_given=False, signed_input=True):
    # Quantize the input tensor
    scale, min_val = tf.quantization.quantize_and_dequantize_v2(
        input_tensor,
        input_min,
        input_max,
        signed_input=signed_input,
        num_bits=num_bits,
        range_given=range_given
    )
    
    # Dequantize the quantized tensor
    dequantized_tensor = tf.quantization.dequantize(
        input_tensor,
        min_val,
        scale,
        axis=-1,
        dtype=tf.float32
    )
    
    return dequantized_tensor

# Example usage:
input_tensor = tf.constant([0.5, 1.0, 1.5], dtype=tf.float32)
input_min = tf.constant(0.0, dtype=tf.float32)
input_max = tf.constant(2.0, dtype=tf.float32)

result = quantize_and_dequantize_tensor(input_tensor, input_min, input_max)
print(result)
