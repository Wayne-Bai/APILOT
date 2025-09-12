import tensorflow as tf

# Define the input dataset
input_dataset = tf.constant([1, 2, 3, 4, 5])

# Define the compression method (e.g., 'gzip')
compression_method = 'gzip'

# Create a compression operation using tf.raw_ops.Compress
compress_op = tf.raw_ops.Compress(
    input=input_dataset,
    compression_method=compression_method,
    output_type=tf.string,
    output_shape=[None]
)

# Run the compression operation
compressed_dataset = compress_op()

# Print the compressed dataset
print(compressed_dataset)
