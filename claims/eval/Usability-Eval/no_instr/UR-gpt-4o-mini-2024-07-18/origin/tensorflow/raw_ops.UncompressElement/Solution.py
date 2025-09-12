import tensorflow as tf

def uncompress_dataset_element(compressed_element):
    # Assuming compressed_element is a serialized tf.data.Dataset element.
    uncompressed_element = tf.raw_ops.Uncompress(compressed_element=compressed_element)
    return uncompressed_element
