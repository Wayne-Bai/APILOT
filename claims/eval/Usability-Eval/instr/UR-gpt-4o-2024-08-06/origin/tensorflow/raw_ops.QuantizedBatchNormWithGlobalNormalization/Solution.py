import tensorflow as tf

def quantized_batch_norm(input_tensor, mean, variance, offset, scale, variance_epsilon):
    """
    Perform quantized batch normalization on the input tensor
    
    :param input_tensor: The input tensor for batch normalization
    :param mean: Mean over all training examples
    :param variance: Variance over all training examples
    :param offset: Offset for the normalized tensor
    :param scale: Scale for the normalized tensor
    :param variance_epsilon: Small float added to variance to avoid dividing by zero

    :return: The batch-normalized output
    """
    # Calculate the batch normalization
    batch_normalized = tf.nn.batch_normalization(
        x=input_tensor,
        mean=mean,
        variance=variance,
        offset=offset,
        scale=scale,
        variance_epsilon=variance_epsilon
    )
    
    # Simulate quantization by casting to a lower precision (e.g., uint8)
    min_val = tf.reduce_min(batch_normalized)
    max_val = tf.reduce_max(batch_normalized)
    quantized = tf.quantization.quantize(
        batch_normalized, min_val, max_val, tf.quint8
    )[0]  # Only the quantized values
    
    return quantized

# Example usage
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
mean = tf.constant([1.5, 2.5], dtype=tf.float32)
variance = tf.constant([0.5, 0.5], dtype=tf.float32)
offset = tf.constant([0.0, 0.0], dtype=tf.float32)
scale = tf.constant([1.0, 1.0], dtype=tf.float32)
variance_epsilon = 1e-5

output_tensor = quantized_batch_norm(input_tensor, mean, variance, offset, scale, variance_epsilon)
print(output_tensor)
