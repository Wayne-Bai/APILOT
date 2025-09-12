import tensorflow as tf

def compute_2d_convolution(input_tensor, filter_tensor, strides, padding):
    """
    Computes a 2-D convolution given 4-D input and filter tensors using TensorFlow's raw ops.

    Args:
    input_tensor (tf.Tensor): A 4-D tensor of shape `[batch, in_height, in_width, in_channels]`
    filter_tensor (tf.Tensor): A 4-D tensor of shape `[filter_height, filter_width, in_channels, out_channels]`
    strides (list of ints): The stride of the sliding window for each dimension of `input_tensor`.
    padding (str): Either "SAME" or "VALID" indicating the type of padding algorithm to use.

    Returns:
    tf.Tensor: A `Tensor` which is the output of the 2-D convolution.
    """
    return tf.raw_ops.Conv2D(input=input_tensor, filter=filter_tensor, strides=strides, padding=padding, use_cudnn_on_gpu=True)

# Example usage:
# Define input features and kernel filter with appropriate shapes
input_features = tf.random.normal([1, 10, 10, 3])  # Example shape: [batch, height, width, channels]
kernel = tf.random.normal([3, 3, 3, 8])  # Example shape: [filter_height, filter_width, in_channels, out_channels]

# Compute convolution
output = compute_2d_convolution(input_features, kernel, strides=[1, 1, 1, 1], padding='SAME')
print(output)
