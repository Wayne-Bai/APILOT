import tensorflow as tf

def create_sparse_cross(sparse_tensors, dense_tensors):
    # Create a list of SparseTensor objects from the sparse_tensors argument
    sparse_inputs = [tf.SparseTensor(sparse_tensor.indices, sparse_tensor.values, sparse_tensor.dense_shape)
                    for sparse_tensor in sparse_tensors]

    # Concatenate the sparse and dense input tensors
    all_inputs = sparse_inputs + dense_tensors

    # Use the tf.raw_ops.SparseCross function to create the SparseCross tensor
    sparse_cross = tf.raw_ops.SparseCross(inputs=all_inputs, num_inputs=len(all_inputs))

    return sparse_cross

# Example usage
sparse_input1 = tf.SparseTensor(indices=[[0, 0, 0], [1, 1, 1]], values=[1, 2], dense_shape=[2, 2, 2])
sparse_input2 = tf.SparseTensor(indices=[[0, 1], [2, 3]], values=[3, 4], dense_shape=[3, 4])
dense_input1 = tf.constant([[0.5], [0.6]])
dense_input2 = tf.constant([[0.1], [0.2]])

sparse_cross = create_sparse_cross([sparse_input1, sparse_input2], [dense_input1, dense_input2])
sparse_cross
