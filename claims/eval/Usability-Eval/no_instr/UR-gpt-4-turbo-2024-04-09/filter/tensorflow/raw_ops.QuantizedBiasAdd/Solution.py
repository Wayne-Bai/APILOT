import tensorflow as tf

def add_quantized_bias(input_tensor, bias_tensor):
    # Calculate the min and max of the input tensor and bias
    input_min, input_max = tf.reduce_min(input_tensor), tf.reduce_max(input_tensor)
    bias_min, bias_max = tf.reduce_min(bias_tensor), tf.reduce_max(bias_tensor)
    
    # Add the bias to the input tensor using quantized addition which requires min and max values
    added_output, added_min, added_max = tf.raw_ops.QuantizedAdd(
        x=input_tensor,
        y=bias_tensor,
        min_x=input_min,
        max_x=input_max,
        min_y=bias_min,
        max_y=bias_max
    )
    
    # Dequantize the result back to float for further use
    dequantized_output = tf.quantization.dequantize(
        added_output, 
        min_range=added_min, 
        max_range=added_max,
        mode='MIN_COMBINED'
    )
    
    return dequantized_output

# Example usage
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.float32)
bias_tensor = tf.constant([0.1, 0.2, 0.3, 0.4], dtype=tf.float32)
output_tensor = add_quantized_bias(input_tensor, bias_tensor)
print(output_tensor)
