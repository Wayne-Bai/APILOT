import tensorflow as tf

# Sample data for the input and the bias
input_tensor = tf.constant([1, 2, 3, 4], dtype=tf.qint32)
bias_tensor = tf.constant([1, 1, 1, 1], dtype=tf.qint32)

# Reshape tensors to ensure they match in dimensions for the addition
input_reshaped = tf.reshape(input_tensor, [2, 2])
bias_reshaped = tf.reshape(bias_tensor, [2, 2])

# Applying the tf.raw_ops.Add operation
output_tensor = tf.raw_ops.QuantizedBiasAdd(
    input=input_reshaped,
    bias=bias_reshaped,
    min_input=-128.0,
    max_input=127.0,
    min_bias=-128.0,
    max_bias=127.0,
    Tinput=tf.qint32,
    out_type=tf.qint32
)

# Running the session to evaluate the output
print("Output Tensor: ", output_tensor)
