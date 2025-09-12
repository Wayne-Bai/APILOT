import tensorflow as tf

# Example usage
raw_dataset = tf.data.Dataset.from_tensor_slices((tf.random.uniform([100, 10], minval=0.0, maxval=1.0, dtype=tf.float32), tf.random.uniform([100], minval=0.0, maxval=1.0, dtype=tf.int32)))

compression_rate = 0.2
compressed_dataset = raw_dataset.map(lambda inputs, labels: tf.raw_ops.raw_compress_datetime(inputs, labels, method=tf.raw_ops.ChainQuote)) # Adjust the compression_rate as needed
