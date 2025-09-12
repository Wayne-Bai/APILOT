import tensorflow as tf

def compress_dataset_element(dataset):
    # Define a function to compress a single element
    def compress_element(element):
        # Assuming the element is a tensor, we can use tf.io.serialize_tensor to serialize it
        serialized_element = tf.io.serialize_tensor(element)
        # Compress the serialized tensor using gzip compression
        compressed_element = tf.io.gfile.GFile.compress(serialized_element.numpy())
        return compressed_element

    # Map the compress_element function over the dataset
    compressed_dataset = dataset.map(lambda x: tf.py_function(compress_element, [x], tf.string))

    return compressed_dataset

# Example usage:
# dataset = ... (your dataset here)
# compressed_dataset = compress_dataset_element(dataset)
