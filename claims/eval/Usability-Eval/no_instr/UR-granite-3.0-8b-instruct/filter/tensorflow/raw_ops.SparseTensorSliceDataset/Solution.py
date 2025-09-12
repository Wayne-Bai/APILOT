import tensorflow as tf

# Assuming you have a SparseTensor named 'sparse_tensor'
def split_sparse_tensor(sparse_tensor):
    # Create a dataset from the SparseTensor
    dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor)

    # Split the dataset row-wise
    split_dataset = dataset.apply(tf.raw_ops.SplitV(num_split=2, axis=1))

    return split_dataset
