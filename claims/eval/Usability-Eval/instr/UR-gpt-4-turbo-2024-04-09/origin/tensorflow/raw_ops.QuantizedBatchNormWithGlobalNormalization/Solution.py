import tensorflow as tf

def quantized_batch_normalization(x, scale, offset, mean, variance, min_range, max_range, variance_epsilon=1e-5):
    # Normalize the input x using the mean and variance
    x_normalized = (x - mean) / tf.sqrt(variance + variance_epsilon)
    # Apply scale and offset (gamma and beta)
    result = x_normalized * scale + offset
    # Quantize the result to the range specified by min_range and max_range
    result_quantized = tf.quantization.quantize(
        result, min_range, max_range, tf.qint32, mode='SCALED'
    )
    # Return quantized tensor
    return result_quantized.output

# Example usage
# Define input tensors
x = tf.constant([10.0, 20.0, 30.0, 40.0], dtype=tf.float32)
scale = tf.constant([0.1, 0.1, 0.1, 0.1], dtype=tf.float32)
offset = tf.constant([1.0, 1.0, 1.0, 1.0], dtype=tf.float32)
mean = tf.constant([15.0, 15.0, 15.0, 15.0], dtype=tf.float32)
variance = tf.constant([4.0, 4.0, 4.0, 4.0], dtype=tf.float32)
min_range = tf.constant(-1.0, dtype=tf.float32)
max_range = tf.constant(1.0, dtype=tf.float32)

result = quantized_batch_normalization(x, scale, offset, mean, variance, min_range, max_range)
print(result)
