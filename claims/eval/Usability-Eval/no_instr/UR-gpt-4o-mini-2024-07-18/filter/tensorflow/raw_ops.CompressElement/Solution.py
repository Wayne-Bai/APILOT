import tensorflow as tf

def compress_dataset_element(dataset_element):
    compressed_element = tf.raw_ops.Compress(dataset_element=dataset_element)
    return compressed_element
