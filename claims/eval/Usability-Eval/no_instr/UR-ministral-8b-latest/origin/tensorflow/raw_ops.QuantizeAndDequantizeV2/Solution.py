import tensorflow as tf

def quantize_dequantize_example():
    # Create a sample tensor
    input_tensor = tf.constant([0.1, 0.5, 1.0, 1.5, 2.0], dtype=tf.float32)

    # Define the method to quantize then dequantize a tensor using tf.raw_ops
    def quantize_dequantize_raw_ops(tensor):
        # Quantize the tensor
        quantized_tensor = tf.raw_ops.Quantize(tensor, mode="sign", dtype=tf.int8)

        # Dequantize the tensor
        dequantized_tensor = tf.raw_ops.Quantize(tensor=quantized_tensor, mode="ps255", dtype=tf.float32)

        return dequantized_tensor

    # Apply the method
    result = quantize_dequantize_raw_ops(input_tensor)

    return result

# Run the example
result = quantize_dequantize_example()
print(result.numpy())  # Print the result after quantization and dequantization
