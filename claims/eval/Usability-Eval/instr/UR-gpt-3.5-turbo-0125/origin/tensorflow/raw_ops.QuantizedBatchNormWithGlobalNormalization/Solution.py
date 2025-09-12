
import tensorflow as tf

def quantized_batch_norm_with_global_normalization(x, scale, offset, mean, variance, old_scale, old_offset, epsilon, name=None):

    def batch_norm_with_global_normalization():
        inv = tf.math.rsqrt(variance + epsilon)
        inv *= scale
        new_scale = inv
        new_offset = offset - mean * inv
        return new_scale, new_offset

    new_scale, new_offset = tf.cond(tf.constant(true), batch_norm_with_global_normalization, lambda: (old_scale, old_offset))
    return tf.nn.quantize_v2(x, new_scale, new_offset, tf.dtypes.quint8)

# Test the function with example inputs
x = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
scale = tf.constant(2.0)
offset = tf.constant(1.0)
mean = tf.constant([0.0, 0.0])
variance = tf.constant([1.0, 1.0])
old_scale = tf.constant(0.5)
old_offset = tf.constant(0.0)
epsilon = 1e-5

output = quantized_batch_norm_with_global_normalization(x, scale, offset, mean, variance, old_scale, old_offset, epsilon)
print(output)
