import tensorflow as tf

# Assuming 'input_tensor' is your input dataset element
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0])

# Define the quantization parameters
min_value = tf.constant(0.0, dtype=tf.float32)
max_value = tf.constant(1.0, dtype=tf.float32)
num_bits = 8
narrow_range = False

# Compress the input tensor using tf.raw_ops.QuantizeV2
compressed_tensor = tf.raw_ops.QuantizeV2(
    input_tensor,
    min_value,
    max_value,
    num_bits,
    narrow_range
)

print(compressed_tensor)
