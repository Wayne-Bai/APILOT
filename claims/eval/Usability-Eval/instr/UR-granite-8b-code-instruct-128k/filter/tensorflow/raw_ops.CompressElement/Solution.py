import tensorflow as tf

def compress_dataset_element(dataset_element):
    # Perform the compression operation on the dataset element
    compressed_element = tf.raw_ops.Compress(input=dataset_element, axis=0)
    return compressed_element
