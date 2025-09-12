import tensorflow as tf

# Define a function for quantization and dequantization
def quantize_and_dequantize_tensor(tensor, num_bits=8):
    """
    Quantizes and dequantizes a tensor using the specified number of bits.
    
    Parameters:
    tensor (tf.Tensor): The input tensor to be quantized and dequantized.
    num_bits (int): Number of bits to use for quantization.
    
    Returns:
    tf.Tensor: The quantized and dequantized tensor.
    """
    # Ensure the tensor is float type (for demonstration)
    tensor = tf.cast(tensor, tf.float32)
    
    # Quantize: Scale to the range [0, 1]
    min_val = tf.reduce_min(tensor)
    max_val = tf.reduce_max(tensor)
    scaled_tensor = (tensor - min_val) / (max_val - min_val)

    # Quantize: Scale to the integer range based on num_bits
    max_int = (1 << num_bits) - 1
    quantized_tensor = tf.round(scaled_tensor * max_int)
    
    # Dequantize: Scale back to the original range
    dequantized_tensor = (quantized_tensor / max_int) * (max_val - min_val) + min_val

    return dequantized_tensor

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    sample_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=tf.float32)
    
    # Apply quantization and dequantization
    result_tensor = quantize_and_dequantize_tensor(sample_tensor, num_bits=8)
    
    # Print the result
    print("Original Tensor:")
    print(sample_tensor)
    print("Quantized and Dequantized Tensor:")
    print(result_tensor)
