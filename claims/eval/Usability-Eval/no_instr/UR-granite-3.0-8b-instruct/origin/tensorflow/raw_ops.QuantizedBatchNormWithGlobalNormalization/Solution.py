import tensorflow as tf

# Define the input tensor
input_tensor = tf.keras.layers.Input(shape=(None, None, 3))

# Perform Quantized Batch Normalization
quantized_batch_norm = tf.raw_ops.QuantizedBatchNormalization(
    input=input_tensor,
    mean=tf.constant([0.0, 0.0, 0.0], dtype=tf.float32),
    variance=tf.constant([1.0, 1.0, 1.0], dtype=tf.float32),
    offset=tf.constant([0.0, 0.0, 0.0], dtype=tf.float32),
    scale=tf.constant([1.0, 1.0, 1.0], dtype=tf.float32),
    min_var=tf.constant(1e-5, dtype=tf.float32),
    epsilon=1e-5,
    data_format='NHWC'
)

# Print the quantized batch normalization output
print(quantized_batch_norm)
