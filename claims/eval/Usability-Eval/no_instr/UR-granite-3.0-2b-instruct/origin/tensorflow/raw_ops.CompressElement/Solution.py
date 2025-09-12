import tensorflow as tf

# Create a 1D tensor
data = tf.constant([1, 2, 3, 4, 5])

# Create a compression parameter (e.g., compression ratio)
compression_ratio = 0.5

# Create a compress operation
compress_op = tf.raw_ops.Compress(
    data=data,
    compression_ratio=compression_ratio,
    name='compress_op'
)

# Run the compress operation
compressed_data = compress_op()

# Print the original and compressed data
print("Original data:", data.numpy())
print("Compressed data:", compressed_data.numpy())
