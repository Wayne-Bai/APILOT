import tensorflow as tf

def quantize_and_dequantize_tensor(tensor, input_range=(-1.0, 1.0), num_bits=8, signed_input=True, narrow_range=False):
    """
    Quantizes and then dequantizes a tensor using TensorFlow.

    Parameters:
    - tensor: the input tensor to be quantized and dequantized.
    - input_range: a tuple specifying the (min, max) range for the tensor values.
    - num_bits: number of bits to use for quantization.
    - signed_input: flag to indicate if the input is signed.
    - narrow_range: whether to use a narrow range for quantization.

    Returns:
    - A tensor that has been quantized and then dequantized.
    """

    # Set the range for quantization
    input_min, input_max = input_range

    # Quantize the tensor
    quantized_tensor = tf.quantization.fake_quant_with_min_max_args(
        inputs=tensor,
        min=input_min,
        max=input_max,
        num_bits=num_bits,
        narrow_range=narrow_range
    )

    # Dequantize the tensor (since we're simulating, this is basically a no-op
    # because the fake quantization simulates the effect of quantization)
    return quantized_tensor

# Example usage
# Create a simple tensor
original_tensor = tf.constant([-1.0, -0.5, 0.0, 0.5, 1.0])
# Quantize and dequantize the tensor
result_tensor = quantize_and_dequantize_tensor(original_tensor)

# Create a session to run the example
tf.compat.v1.disable_eager_execution() # Disable eager if not using tf 2.x eager execution by default
with tf.compat.v1.Session() as sess:
    print("Original Tensor:", sess.run(original_tensor))
    print("Quantized and Dequantized Tensor:", sess.run(result_tensor))
