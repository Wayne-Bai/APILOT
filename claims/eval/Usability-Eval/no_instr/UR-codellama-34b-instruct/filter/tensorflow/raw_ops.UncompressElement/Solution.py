import tensorflow as tf

# Load the compressed dataset using TensorFlow's raw operations
compressed_dataset = tf.data.experimental.load(
    filename="path/to/compressed/dataset",
    compression=None,
)

# Uncompress the loaded dataset using TensorFlow's built-in uncompression operation
uncompressed_dataset = tf.raw_ops.Uncompress(
    input=compressed_dataset,
    compressed_data_format="",
    compression_method="",
)
