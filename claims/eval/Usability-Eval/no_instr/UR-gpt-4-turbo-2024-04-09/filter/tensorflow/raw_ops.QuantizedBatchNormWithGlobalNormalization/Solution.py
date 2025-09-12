import tensorflow as tf

def quantized_batch_norm(x, mean, variance, offset, scale, variance_epsilon, min_range, max_range):
    """
    Perform quantized batch normalization on input tensor x using given parameters.

    Parameters:
    - x : Tensor, input feature batch.
    - mean : Tensor, mean for normalization.
    - variance : Tensor, variance for normalization.
    - offset : Tensor, offset to apply.
    - scale : Tensor, scale parameter.
    - variance_epsilon : float, small float for numerical stability.
    - min_range : float, minimum value of range used for quantization.
    - max_range : float, maximum value of range used for quantization.

    Returns:
    - Tensor, the normalized and rescaled output.
    - Tensor, the quantization range (min_value, max_value).
    """
    x_norm = tf.nn.batch_normalization(x, mean, variance, offset, scale, variance_epsilon)
    x_quantized = tf.quantization.quantize(x_norm, min_range, max_range, tf.qint32)
    return x_quantized

# Example usage
input_tensor = tf.constant([10, 20, 30, 40, 50], dtype=tf.float32)
mean_tensor = tf.constant([20], dtype=tf.float32)
variance_tensor = tf.constant([25], dtype=tf.float32)
offset_tensor = tf.constant([0], dtype=tf.float32)
scale_tensor = tf.constant([1], dtype=tf.float32)
variance_epsilon = 0.001
min_range = -6
max_range = 6

# Quantized Batch Normalization
quantized_output = quantized_batch_norm(input_tensor, mean_tensor, variance_tensor, offset_tensor, scale_tensor, variance_epsilon, min_range, max_range)
print(quantized_output)  # Outputs quantized tensor info
