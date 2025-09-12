import tensorflow as tf

# Create a simple dataset
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Define the compression function
def compress_element(element):
    return tf.io.compress(element, compression_type='ZLIB')

# Apply the compression function to the dataset
compressed_dataset = dataset.map(compress_element)

# Print the compressed dataset
for element in compressed_dataset:
    print(element)
