import tensorflow as tf

def quantized_bias_add(input_tensor, bias_tensor):
    """
    Adds Tensor 'bias' to Tensor 'input' for Quantized types.
    
    Args:
    input_tensor (tf.Tensor): Input tensor to add bias to.
    bias_tensor (tf.Tensor): Bias tensor to add.
    
    Returns:
    tf.Tensor: The result of adding 'bias' to 'input'.
    """
    
    # Check if both tensors are quantized
    if input_tensor.dtype!= tf.quint8 and input_tensor.dtype!= tf.qint8 and input_tensor.dtype!= tf.qint32 and input_tensor.dtype!= tf.quint32:
        raise ValueError("Input tensor must be a quantized type.")
        
    if bias_tensor.dtype!= tf.quint8 and bias_tensor.dtype!= tf.qint8 and bias_tensor.dtype!= tf.qint32 and bias_tensor.dtype!= tf.quint32:
        raise ValueError("Bias tensor must be a quantized type.")
        
    # Get the minimum and maximum values for input and bias tensors
    input_min = tf.reduce_min(input_tensor)
    input_max = tf.reduce_max(input_tensor)
    bias_min = tf.reduce_min(bias_tensor)
    bias_max = tf.reduce_max(bias_tensor)
    
    # Calculate the output range
    output_min = tf.math.add(input_min, bias_min)
    output_max = tf.math.add(input_max, bias_max)
    
    # Clip the output to the valid range for quantized types
    output = tf.clip_by_value(tf.math.add(input_tensor, bias_tensor), output_min, output_max)
    
    # Return the result
    return output

# Example usage
if __name__ == "__main__":
    # Create a quantized input tensor
    input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.quint8)
    
    # Create a quantized bias tensor
    bias_tensor = tf.constant([0.5, 0.5, 0.5, 0.5], dtype=tf.quint8)
    
    # Add the bias to the input tensor
    result = quantized_bias_add(input_tensor, bias_tensor)
    
    print(result)
