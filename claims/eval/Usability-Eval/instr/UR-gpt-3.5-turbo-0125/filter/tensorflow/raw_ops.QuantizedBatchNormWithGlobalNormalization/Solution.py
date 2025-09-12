
import tensorflow as tf

def quantized_batch_norm(inputs, scale, offset, mean, variance, offset_adj, scale_adj, variance_adj, epsilon=0.0001):
    return tf.raw_ops.QuantizedBatchNormWithGlobalNormalization(t=tf.float32, t_min=tf.quint8, t_min_adjust=tf.float32, inputs=inputs, scale=scale, offset=offset, mean=mean, variance=variance, offset_adj=offset_adj, scale_adj=scale_adj, variance_adj=variance_adj, epsilon=epsilon)

# Example usage
inputs = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
scale = tf.constant(0.5, dtype=tf.float32)
offset = tf.constant(0, dtype=tf.float32)
mean = tf.constant(2, dtype=tf.float32)
variance = tf.constant(1, dtype=tf.float32)
offset_adj = tf.constant(0, dtype=tf.float32)
scale_adj = tf.constant(1, dtype=tf.float32)
variance_adj = tf.constant(1, dtype=tf.float32)

result = quantized_batch_norm(inputs, scale, offset, mean, variance, offset_adj, scale_adj, variance_adj)
print(result)
