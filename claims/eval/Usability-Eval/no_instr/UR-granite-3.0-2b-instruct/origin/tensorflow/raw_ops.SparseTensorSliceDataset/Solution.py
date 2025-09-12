import tensorflow as tf

def create_row_wise_dataset(sparse_tensor):
    # Convert SparseTensor to dense tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor)

    # Reshape the dense tensor to row-wise format
    row_wise_tensor = tf.reshape(dense_tensor, [-1, tf.shape(dense_tensor)[1]])

    # Create a dataset from the row-wise tensor
    dataset = tf.data.Dataset.from_tensor_slices(row_wise_tensor)

    return dataset
