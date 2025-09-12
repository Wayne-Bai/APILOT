import tensorflow as tf

# Define a TensorFlow constant representing the dataset
dataset = tf.constant([1, 2, 3, 4, 5])

# Create a method to compress the dataset using tf.raw_ops.DataSetCompression
@tf.function
def compress_dataset():
    return tf.raw_ops.DataSetCompression(dataset)

# Invoke the compression method
compressed_dataset = compress_dataset(dataset)
print(compressed_dataset)
