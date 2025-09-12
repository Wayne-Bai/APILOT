import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[[[1.0], [2.0], [3.0]],
                             [[4.0], [5.0], [6.0]],
                             [[7.0], [8.0], [9.0]]]], dtype=tf.float32)

# Define the pooling window size for each dimension
pooling_ratio = [1.0, 1.44, 1.44, 1.0]  # Typically, the batch and channel dimensions are 1.0

# Perform fractional average pooling
output, row_pooling_sequence, col_pooling_sequence = tf.nn.fractional_avg_pool(
    value=input_tensor,
    pooling_ratio=pooling_ratio,
    pseudo_random=True,  # For the sequence to be generated in a pseudo-random fashion
    overlapping=True  # Whether the pooling cells can overlap
)

# Run the session to compute the result
print("Input:")
print(input_tensor.numpy())
print("\nOutput:")
print(output.numpy())
