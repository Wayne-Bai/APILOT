
import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_split, axis):
    sparse_values = tf.sparse.split(sp_input=sparse_tensor, axis=axis, num_split=num_split)
    
    return sparse_values
  
# Usage example
indices = tf.constant([[0, 0], [1, 2], [3, 1]])
values = tf.constant([1.0, 2.0, 3.0])
dense_shape = [4, 3]
sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

num_split = 2
axis = 0
split_tensors = split_sparse_tensor(sparse_tensor, num_split, axis)
