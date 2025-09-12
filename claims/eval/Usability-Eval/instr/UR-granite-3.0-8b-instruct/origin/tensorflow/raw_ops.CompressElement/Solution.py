import tensorflow as tf

# Assuming 'input_data' is your dataset element
input_data = tf.constant([[1, 2, 3], [4, 5, 6]])

# Using tf.raw_ops.QuantizeDownAndTrim to compress the dataset element
quantized_data = tf.raw_ops.QuantizeDownAndTrim(
    input_tensor=input_data,
    min_range=0,
    max_range=255,
    num_bits=8,
    narrow_range=True
)

print(quantized_data)
