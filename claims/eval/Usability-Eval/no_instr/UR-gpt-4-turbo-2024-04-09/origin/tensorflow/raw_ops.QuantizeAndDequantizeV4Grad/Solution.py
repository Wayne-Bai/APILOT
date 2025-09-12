import tensorflow as tf

def gradient_of_quantize_and_dequantize_v4(input_tensor, input_min, input_max, num_bits, range_given, signed_input, narrow_range):
    with tf.GradientTape() as tape:
        tape.watch(input_tensor)
        output = tf.raw_ops.QuantizeAndDequantizeV4(
            input=input_tensor,
            input_min=input_min,
            input_max=input_max,
            num_bits=num_bits,
            range_given=range_given,
            signed_input=signed_input,
            narrow_range=narrow_range
        )
    gradient = tape.gradient(output, input_tensor)
    return gradient

# Example usage:
input_tensor = tf.constant([1.0, 2.5, 3.0, 4.5], dtype=tf.float32)
input_min = tf.reduce_min(input_tensor)
input_max = tf.reduce_max(input_tensor)
num_bits = 8
range_given = True
signed_input = True
narrow_range = False

gradient = gradient_of_quantize_and_dequantize_v4(input_tensor, input_min, input_max, num_bits, range_given, signed_input, narrow_range)
print("Gradient:", gradient)
