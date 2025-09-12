import tensorflow as tf

def quantize_and_dequantize_v4_grad(grad, input, input_min, input_max, signed_input=True, num_bits=8, range_given=False, round_mode="HALF_TO_EVEN", narrow_range=False, axis=-1):
    with tf.GradientTape() as tape:
        tape.watch([input, input_min, input_max])
        quantized_output = tf.quantization.quantize_and_dequantize_v2(
            input, input_min, input_max, signed_input=signed_input, num_bits=num_bits, range_given=range_given, round_mode=round_mode, narrow_range=narrow_range, axis=axis
        )
    grad_input, grad_input_min, grad_input_max = tape.gradient(quantized_output, [input, input_min, input_max], output_gradients=grad)
    return grad_input, grad_input_min, grad_input_max

# Example usage:
# grad = tf.random.normal(shape=input.shape)
# grad_input, grad_input_min, grad_input_max = quantize_and_dequantize_v4_grad(grad, input, input_min, input_max)
