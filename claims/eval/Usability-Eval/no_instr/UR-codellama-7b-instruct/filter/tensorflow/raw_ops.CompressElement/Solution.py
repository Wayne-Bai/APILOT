
import tensorflow as tf

# Define the input data
data = tf.constant([[1, 2], [3, 4]])

# Define the compression parameters
compression_level = 5
bit_width = 8
signed = True

# Compress the data using the TensorFlow raw ops
result = tf.raw_ops.CompressDataset(
    input=data,
    compression=tf.CompressionType.GZIP,
    compression_level=compression_level,
    bit_width=bit_width,
    signed=signed
)

# Print the compressed data
print(result)
