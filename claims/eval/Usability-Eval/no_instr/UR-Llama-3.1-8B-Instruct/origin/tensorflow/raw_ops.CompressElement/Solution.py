# Import necessary libraries
import tensorflow as tf
import numpy as np

# Define a function to create a sample dataset
def create_dataset():
    # Create a simple dataset with a list of numbers
    dataset = tf.data.Dataset.from_tensor_slices([10, 20, 30, 40, 50])
    return dataset

# Define a function to compress the dataset elements
def compress_dataset(dataset, compression_type):
    # Define different compression methods
    compression_methods = {
        'lz4': tf.data.Options().jit_level(1). ExperimentalLZ4CompressionFormat(),
        'zlib': tf.data.Options().jit_level(1).ExperimentalZLIBCompressionFormat()
    }
    
    # Return the dataset with the given compression type
    if compression_type in compression_methods:
        return dataset.with_options(compression_methods[compression_type])
    else:
        raise ValueError('Invalid compression type. Supported types are lz4 and zlib.')

# Create a sample dataset
dataset = create_dataset()
print("Original Dataset:")
print(dataset)

# Compress the dataset using lz4 compression
compressed_dataset = compress_dataset(dataset, 'lz4')

# Print the compressed dataset
print("\nCompressed Dataset (lz4):")
print(compressed_dataset)

# Compress the dataset using zlib compression
compressed_dataset_zlib = compress_dataset(dataset, 'zlib')

# Print the compressed dataset
print("\nCompressed Dataset (zlib):")
print(compressed_dataset_zlib)
