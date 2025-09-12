import tensorflow as tf

def quantized_bias_add(input_tensor, bias_tensor, min_input, max_input, min_bias, max_bias):
    """
    Adds bias to input tensors with quantization consideration.
    
    :param input_tensor: The input tensor, quantized type.
    :param bias_tensor: The bias tensor, should be quantized.
    :param min_input: The minimum value of the input tensor after quantization.
    :param max_input: The maximum value of the input tensor after quantization.
    :param min_bias: The minimum value of the bias tensor after quantization.
    :param max_bias: The maximum value of the bias tensor after quantization.
    
    :return: A tuple of (output_tensor, min_output, max_output)
    """
    
    # Calculate the scale factors
    input_scale = (max_input - min_input) / 255.0
    bias_scale = (max_bias - min_bias) / 255.0

    output_min = min_input + min_bias
    output_max = max_input + max_bias
    
    # Scale tensors to regular floats
    input_float = tf.cast(input_tensor, tf.float32) * input_scale + min_input
    bias_float = tf.cast(bias_tensor, tf.float32) * bias_scale + min_bias

    # Perform the bias addition
    output_float = input_float + bias_float

    # Determine scale for output
    output_scale = (output_max - output_min) / 255.0

    # Quantize the output back to integer type
    output_tensor = tf.cast((output_float - output_min) / output_scale, tf.qint32)
    
    return output_tensor, output_min, output_max

# Example usage
input_image = tf.constant([1, 2, 3], dtype=tf.qint32)
bias = tf.constant([1], dtype=tf.qint32)

min_input = 0.0
max_input = 1.0

min_bias = 0.0
max_bias = 1.0

output, output_min, output_max = quantized_bias_add(input_image, bias, min_input, max_input, min_bias, max_bias)
print("Output Tensor:", output)
print("Output Min:", output_min)
print("Output Max:", output_max)
