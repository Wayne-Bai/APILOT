import tensorflow as tf

def quantize_and_dequantize_v4_grad(grad, input, input_min, input_max, axis, signed_input, num_bits, range_given, round_mode, narrow_range, axis_given):
    # Implement the gradient for QuantizeAndDequantizeV4
    with tf.GradientTape() as tape:
        tape.watch([input, input_min, input_max])
        quantized = tf.quantization.quantize_and_dequantize_v4(
            input, input_min, input_max, axis=axis, signed_input=signed_input,
            num_bits=num_bits, range_given=range_given, round_mode=round_mode,
            narrow_range=narrow_range, axis_given=axis_given
        )
    
    grad_input, grad_input_min, grad_input_max = tape.gradient(quantized, [input, input_min, input_max], output_gradients=grad)
    
    return grad_input, grad_input_min, grad_input_max

# Example usage:
# grad = tf.ones_like(input)  # Example gradient
# grad_input, grad_input_min, grad_input_max = quantize_and_dequantize_v4_grad(grad, input, input_min, input_max, axis, signed_input, num_bits, range_given, round_mode, narrow_range, axis_given)
