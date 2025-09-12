import tensorflow as tf

def compress_dataset_element(dataset):
    compressed_dataset = dataset.map(lambda x: tf.raw_ops.Compress(tensor=x))
    return compressed_dataset

# Example usage
# Assuming 'dataset' is a tf.data.Dataset object:
# dataset = tf.data.Dataset.from_tensor_slices([...])
# compressed_dataset = compress_dataset_element(dataset)
