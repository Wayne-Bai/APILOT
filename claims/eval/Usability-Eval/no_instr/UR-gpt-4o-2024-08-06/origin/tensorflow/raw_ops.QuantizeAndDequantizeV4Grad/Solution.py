import tensorflow as tf

# Define a custom operation to calculate the gradient of QuantizeAndDequantizeV4
@tf.custom_gradient
def quantize_and_dequantize_v4_gradient(x, input_min, input_max, num_bits, signed_input=True, range_given=False, narrow_range=False, axis=None):
    # Perform the forward operation: Quantize and Dequantize
    y = tf.raw_ops.QuantizeAndDequantizeV4(
        input=x,
        input_min=input_min,
        input_max=input_max,
        num_bits=num_bits,
        signed_input=signed_input,
        range_given=range_given,
        narrow_range=narrow_range,
        axis=axis
    )

    # Custom gradient function
    def grad(dy):
        # Simply pass through the gradient for this example
        # More sophisticated gradient logic might be required in real cases
        return (
            dy,                    # Gradient w.r.t `x`
            tf.zeros_like(input_min),  # No gradient contribution for scalars
            tf.zeros_like(input_max),  # No gradient contribution for scalars
            tf.zeros_like(num_bits),   # No gradient contribution for scalars
            None,                      # signed_input is a boolean constant
            None,                      # range_given is a boolean constant
            None,                      # narrow_range is a boolean constant
            None                       # axis is a constant
        )

    return y, grad

# Example usage
input_tensor = tf.constant([0.1, 0.5, 0.9], dtype=tf.float32)
input_min = 0.0
input_max = 1.0
num_bits = 8

# Use the custom operation
quantized_dequantized_output = quantize_and_dequantize_v4_gradient(input_tensor, input_min, input_max, num_bits)

print("Output", quantized_dequantized_output)
