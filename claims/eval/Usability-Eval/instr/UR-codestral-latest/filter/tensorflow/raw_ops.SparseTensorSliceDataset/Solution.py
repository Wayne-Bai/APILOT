import tensorflow as tf

def split_sparse_tensor(sparse_tensor):
    # Create a dataset from the indices of the sparse tensor
    indices_dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor.indices)

    # Create a dataset from the values of the sparse tensor
    values_dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor.values)

    # Create a dataset from the dense shape of the sparse tensor
    # We'll use this to reshape each row
    dense_shape_dataset = tf.data.Dataset.from_tensors(sparse_tensor.dense_shape)

    # Zip the indices and values datasets together
    data_dataset = tf.data.Dataset.zip((indices_dataset, values_dataset))

    # Group the data by row index
    def key_func(index, _):
        return index[0]

    def reduce_func(key, windowed_data):
        indices = [index for index, _ in windowed_data]
        values = [value for _, value in windowed_data]
        row_indices = [index[1:] for index in indices]
        shape = [dense_shape_dataset.as_numpy_iterator().next()[1]] + sparse_tensor.shape[1:]
        row_sparse_tensor = tf.SparseTensor(indices=row_indices, values=values, dense_shape=shape)
        return row_sparse_tensor

    row_dataset = data_dataset.group_by_window(key_func, reduce_func, window_size=None)

    return row_dataset
