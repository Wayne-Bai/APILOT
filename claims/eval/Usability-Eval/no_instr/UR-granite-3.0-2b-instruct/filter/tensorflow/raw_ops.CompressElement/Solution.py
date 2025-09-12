import tensorflow as tf

# Define the input dataset
input_dataset = tf.constant([1, 2, 3, 4, 5])

# Define the compression method (e.g., quantization)
compression_method = tf.raw_ops.Compression(quantize_type='INT8')

# Apply the compression method to the input dataset
compressed_dataset = compression_method(input_dataset)

# Print the original and compressed datasets
print("Original dataset:")
print(input_dataset.numpy())
print("\nCompressed dataset:")
print(compressed_dataset.numpy())
