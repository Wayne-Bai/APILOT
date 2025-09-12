import tensorflow as tf

def compress_data_element(dataset_element):
    # Assuming the dataset_element is a tensor containing binary data (0s and 1s)
    # Here we are using a simple example where we remove elements if they are 0

    # Define a filter operation to remove elements equal to 0
    compressed_element = tf.boolean_mask(dataset_element, tf.not_equal(dataset_element, 0))

    return compressed_element

# Dummy dataset element for demonstration
dummy_element = tf.constant([1, 3, 0, 5, 0, 7], dtype=tf.int32)

# Compress the dataset element
compressed_element = compress_data_element(dummy_element)

# Run the operation and print the result
print(compressed_element.numpy())
