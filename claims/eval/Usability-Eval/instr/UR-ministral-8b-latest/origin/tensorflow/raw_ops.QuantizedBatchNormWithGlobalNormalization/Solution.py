import tensorflow as tf

# Define the custom method as a TensorFlow quantized batch normalization
def custom_quantized_batch_norm(inputs, axis, momentum=0.99, epsilon=1e-5, scale=True, center=True):
    # Create a TensorFlow operation for quantization-aware training
    ref = tf.raw_ops.QATBatchNorm(
        inputs,
        features,
        axis,
        momentum=momentum,
        training=True,
        center=center,
        scale=scale,
        epsilon=epsilon,
       shift=False
    )
    return ref

# Example usage
x_input = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
features = x_input.shape[-1]
output = custom_quantized_batch_norm(x_input, axis=-1)
print(output)
