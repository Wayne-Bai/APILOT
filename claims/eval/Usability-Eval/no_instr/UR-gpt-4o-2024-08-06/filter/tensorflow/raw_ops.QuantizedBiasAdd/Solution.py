import tensorflow as tf

# Function to add quantized bias to a quantized input
def quantized_bias_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias):
    # Define the data types for quantization
    T1 = tf.qint32
    T2 = tf.qint32
    out_type = tf.qint32

    # Convert input and bias tensors to the specified quantized types
    quantized_input = tf.quantization.fake_quant_with_min_max_vars(
        input_tensor, min=min_input, max=max_input, num_bits=8, narrow_range=False
    )
    quantized_bias = tf.quantization.fake_quant_with_min_max_vars(
        bias_tensor, min=min_bias, max=max_bias, num_bits=8, narrow_range=False
    )

    # Use tf.nn.bias_add to perform the addition of bias to the input
    result = tf.nn.bias_add(quantized_input, quantized_bias)

    # Optionally, re-quantize the output based on the output type range
    # Here we're using tf.quantization.quantize_and_dequantize for demonstration
    result_quantized = tf.quantization.quantize_and_dequantize(
        result, min_input, max_input, out_type=out_type
    )

    return result_quantized

# Example usage
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
bias_tensor = tf.constant([0.5, -0.5], dtype=tf.float32)
min_input, max_input = 0.0, 5.0
min_bias, max_bias = -1.0, 1.0

# Applying quantized bias addition
result_tensor = quantized_bias_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias)
print(result_tensor.numpy())
