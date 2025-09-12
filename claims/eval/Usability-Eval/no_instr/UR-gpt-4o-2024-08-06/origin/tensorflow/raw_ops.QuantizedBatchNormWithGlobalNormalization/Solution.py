import tensorflow as tf

# Assuming you have a quantized input tensor `quantized_input`, a set of other required parameters.
quantized_input = tf.constant([100, 150, 200], dtype=tf.qint32)
mean = tf.constant([0.5], dtype=tf.float32)
variance = tf.constant([0.1], dtype=tf.float32)
offset = tf.constant([1.0], dtype=tf.float32)
scale = tf.constant([0.1], dtype=tf.float32)
min_range = tf.constant([0.0], dtype=tf.float32)
max_range = tf.constant([1.0], dtype=tf.float32)

# Quantized batch normalization operation
output, min_output, max_output = tf.raw_ops.QuantizedBatchNormWithGlobalNormalization(
    t=quantized_input,
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
    variance_epsilon=1e-5,
    scale_after_normalization=True
)

# To evaluate and print the result you would need to run in a TensorFlow session/environment
# Below is an example for running in a TensorFlow 1.x-like session style in 2.x just for demonstration
tf.print("Output:", output)
tf.print("Min Output:", min_output)
tf.print("Max Output:", max_output)
