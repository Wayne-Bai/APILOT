import tensorflow as tf

# Function to quantize and then dequantize a tensor
def quantize_and_dequantize_tensor(tensor):
    # Quantize the tensor
    quantized_tensor = tf.quantization.fake_quant_with_min_max_args(
        inputs=tensor, min=-1.0, max=1.0, num_bits=8
    )
    
    # Dequantize the tensor (for display, it's the same tensor as quantized because tf does not use a 'real' quantize step in this function)
    dequantized_tensor = quantized_tensor  # Fake quantization already performs the step

    return dequantized_tensor

# Example tensor
example_tensor = tf.constant([0.5, 0.2, -0.1, 0.0, 1.0, -0.5], dtype=tf.float32)

# Quantize and dequantize the example tensor
quantized_and_dequantized = quantize_and_dequantize_tensor(example_tensor)

# Start a session to print the results (if using TF 1.x, since TF 2.x uses eager execution by default)
tf.print("Original Tensor:", example_tensor)
tf.print("Quantized and Dequantized Tensor:", quantized_and_dequantized)
