import tensorflow as tf

def compress_dataset_element(dataset):
    # Use tf.data.experimental.CsvDataset to load the dataset
    dataset = tf.data.experimental.CsvDataset(file_pattern, record_defaults, header=True, field_delim=',')

    # Map each element to a numpy array
    dataset = dataset.map(lambda x: tf.numpy_function(func=lambda: np.array(x.numpy()), inp=[], Tout=tf.float64))

    # Use tf.data.Dataset.from_tensor_slices to compress the dataset
    compressed_dataset = tf.data.Dataset.from_tensor_slices(dataset)

    return compressed_dataset
