import tensorflow as tf

def quantized_bias_add(input_tensor, bias_tensor, input_min, input_max, bias_min, bias_max):
    # Cast input and bias tensors to float32 for addition
    input_tensor_float = tf.cast(input_tensor, tf.float32)
    bias_tensor_float = tf.cast(bias_tensor, tf.float32)
    
    # Perform the addition in float32
    result_float = input_tensor_float + bias_tensor_float
    
    # Quantize the result back to the original input type
    result_quantized = tf.quantization.fake_quant_with_min_max_args(
        result_float, min=input_min, max=input_max, num_bits=8, narrow_range=False
    )
    
    return result_quantized

# Example usage:
# input_tensor = ...  # Your quantized input tensor
# bias_tensor = ...   # Your quantized bias tensor
# input_min = ...     # Minimum value of the input tensor
# input_max = ...     # Maximum value of the input tensor
# bias_min = ...      # Minimum value of the bias tensor
# bias_max = ...      # Maximum value of the bias tensor

# result = quantized_bias_add(input_tensor, bias_tensor, input_min, input_max, bias_min, bias_max)
