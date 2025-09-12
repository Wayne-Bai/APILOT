import tensorflow as tf

def quantized_batch_normalization(x, mean, variance, scale, offset, variance_epsilon, min_range, max_range):
    # Quantized batch normalization using global normalization.
    normalized, output_min, output_max = tf.raw_ops.QuantizedBatchNormWithGlobalNormalization(
        t=x, 
        t_min=min_range, 
        t_max=max_range, 
        m=mean,
        m_min=min_range, 
        m_max=max_range,
        v=variance,
        v_min=min_range,
        v_max=max_range,
        beta=offset,
        beta_min=min_range,
        beta_max=max_range,
        gamma=scale,
        gamma_min=min_range,
        gamma_max=max_range,
        variance_epsilon=variance_epsilon,
        scale_after_normalization=True
    )

    return normalized, output_min, output_max

# Example usage:
x = tf.constant([10.0, 20.0, 30.0, 40.0], dtype=tf.float32)
mean = tf.constant([20.0], dtype=tf.float32)
variance = tf.constant([5.0], dtype=tf.float32)
scale = tf.constant([0.1], dtype=tf.float32)
offset = tf.constant([0.5], dtype=tf.float32)
variance_epsilon = 0.001
min_range = tf.constant([0], dtype=tf.float32)
max_range = tf.constant([50], dtype=tf.float32)

normalized, output_min, output_max = quantized_batch_normalization(
    x, mean, variance, scale, offset, variance_epsilon, min_range, max_range
)

tf.print("Normalized:", normalized)
tf.print("Output Min:", output_min)
tf.print("Output Max:", output_max)
