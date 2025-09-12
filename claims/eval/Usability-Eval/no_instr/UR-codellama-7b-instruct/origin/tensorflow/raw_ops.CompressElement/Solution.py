
import tensorflow as tf

# Define the input data
data = np.array([[1., 2.], [3., 4.]])

# Compress the data using the raw ops module
compressed_data = tf.raw_ops.Compress(
    input=tf.constant(data),
    algorithm="gzip",
    level=6,
)

# Print the compressed data
print(compressed_data.numpy())
