import tensorflow as tf

def quantized_batch_norm(inputs, mean, variance, offset, scale, variance_epsilon=1e-5, is_training=False):
    # Applying Quantized Batch Normalization
    outputs = tf.quantization.quantize(
        tf.nn.batch_normalization(inputs, mean, variance, offset, scale, variance_epsilon),
        min_range=0, 
        max_range=6, 
        T=tf.quint8, 
        mode='SCALED')
    
    return outputs

# Example Usage:
inputs = tf.constant([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
mean = tf.constant([2.0, 3.0], dtype=tf.float32)
variance = tf.constant([1.0, 1.0], dtype=tf.float32)
offset = tf.constant([0.0, 0.0], dtype=tf.float32)
scale = tf.constant([1.0, 1.0], dtype=tf.float32)

output = quantized_batch_norm(inputs, mean, variance, offset, scale)
print(output)
