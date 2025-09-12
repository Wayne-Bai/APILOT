import tensorflow as tf

# Define a function to uncompress a dataset element using the UncompressElement op
def uncompress_element(compressed_data, output_types, output_shapes, compression_type=''):
    # Create a TensorFlow dataset from the compressed data
    compressed_tensor = tf.constant(compressed_data, dtype=tf.string)
    dataset = tf.data.Dataset.from_tensor_slices(compressed_tensor)
    
    # Map the UncompressElement function on the dataset
    def uncompress_fn(value):
        return tf.raw_ops.UncompressElement(
            input=value,
            output_types=output_types,
            output_shapes=output_shapes,
            compression_type=compression_type
        )
    
    uncompressed_dataset = dataset.map(uncompress_fn)

    return uncompressed_dataset

# Example Usage
# Define the input compressed data, types, and shapes of the dataset
# Note: In a real case, provide actual compressed data and type/shape info
compressed_data_example = ['gzipped_data1', 'gzipped_data2']
output_types_example = [tf.string]
output_shapes_example = [()]

# Uncompress the dataset elements
uncompressed_dataset = uncompress_element(
    compressed_data=compressed_data_example,
    output_types=output_types_example,
    output_shapes=output_shapes_example,
    compression_type='GZIP'  # Example compression type
)

# Iterate over the uncompressed dataset
for element in uncompressed_dataset:
    print(element.numpy())
