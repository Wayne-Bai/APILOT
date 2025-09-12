import tensorflow as tf

# Define a function to quantize and dequantize a tensor
def quantize_and_dequantize_tensor(tensor, input_min, input_max, num_bits=8):
    # Quantize the input tensor to the specified range using uniform quantization
    quantized = tf.quantization.fake_quant_with_min_max_args(
        inputs=tensor, min=input_min, max=input_max, num_bits=num_bits)
    
    # Dequantize by simply simulating the reverse process using the same function
    # In this case, it's just a simulation as tensorflow fake_quant handles both operations
    return quantized

# Example usage
if __name__ == "__main__":
    # Create a sample tensor
    sample_tensor = tf.constant([0.1, 0.5, 0.8, 0.4], dtype=tf.float32)
    
    # Define the minimum and maximum range for quantization
    input_min = 0.0
    input_max = 1.0
    
    # Quantize and dequantize the sample tensor
    result_tensor = quantize_and_dequantize_tensor(sample_tensor, input_min, input_max)
    
    # Run in a session and print
    print("Original Tensor: ", sample_tensor.numpy())
    print("Quantize and Dequantize Result: ", result_tensor.numpy())
