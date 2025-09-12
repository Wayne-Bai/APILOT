import tensorflow as tf

def compress_dataset_element(dataset):
    # Assuming dataset is a TensorFlow dataset
    def compress_element(element):
        # Convert the element to a string representation
        element_str = tf.io.serialize_tensor(element)
        # Compress the string representation using gzip
        compressed_element = tf.io.gzip_compress(element_str)
        return compressed_element

    # Map the compress_element function over the dataset
    compressed_dataset = dataset.map(compress_element)
    return compressed_dataset

# Example usage:
# dataset = ... (your TensorFlow dataset)
# compressed_dataset = compress_dataset_element(dataset)
