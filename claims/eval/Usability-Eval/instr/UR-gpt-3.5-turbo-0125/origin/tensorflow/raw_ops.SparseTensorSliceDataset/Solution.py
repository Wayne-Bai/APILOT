
import tensorflow as tf

def create_sparse_split_dataset(sparse_input, num_splits):
    split_data = tf.raw_ops.SparseSplit(indices=sparse_input.indices,
                                        values=sparse_input.values,
                                        shapes=sparse_input.dense_shape,
                                        num_splits=num_splits)
    return split_data

# Example of how to use the function
sparse_input = tf.sparse.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]],
                                      values=[1.0, 2.0, 3.0],
                                      dense_shape=[3, 3])

num_splits = 3
split_dataset = create_sparse_split_dataset(sparse_input, num_splits)
