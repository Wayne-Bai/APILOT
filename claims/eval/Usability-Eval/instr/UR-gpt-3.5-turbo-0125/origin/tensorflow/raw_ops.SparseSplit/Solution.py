
import tensorflow as tf

def split_sparse_tensor(input_sparse_tensor, num_split, split_dim):
    outputs = tf.raw_ops.Split(
        split_dim=split_dim,
        num_split=num_split,
        value=input_sparse_tensor.values,
        indices=input_sparse_tensor.indices
    )
    
    split_sparse_tensors = []
    for i in range(num_split):
        split_sparse_tensors.append(tf.SparseTensor(
            indices=outputs[i].indices,
            values=outputs[i].values,
            dense_shape=input_sparse_tensor.dense_shape
        ))
    
    return split_sparse_tensors

# Usage example
input_sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]],
                                      values=[1.0, 2.0, 3.0],
                                      dense_shape=[3, 3])
num_split = 2
split_dim = 1

split_sparse_tensors = split_sparse_tensor(input_sparse_tensor, num_split, split_dim)
