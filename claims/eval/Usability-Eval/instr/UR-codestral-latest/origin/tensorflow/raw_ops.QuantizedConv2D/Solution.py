import tensorflow as tf

def quantize_tensor(input_tensor):
    # This function will depend on your specific use case and data.
    # For this example, let's assume it simply returns the input tensor.
    return input_tensor

def compute_convolution(input_tensor, filter_tensor):
    # Quantize input and filter tensors
    input_tensor_quantized = quantize_tensor(input_tensor)
    filter_tensor_quantized = quantize_tensor(filter_tensor)

    # Compute 2D convolution
    output_tensor = tf.nn.conv2d(input_tensor_quantized, filter_tensor_quantized, strides=[1, 1, 1, 1], padding='SAME')

    return output_tensor
