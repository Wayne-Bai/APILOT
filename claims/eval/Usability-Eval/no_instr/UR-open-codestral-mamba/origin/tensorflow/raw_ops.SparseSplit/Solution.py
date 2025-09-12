import tensorflow as tf

# Assuming we have a SparseTensor named 'sparse_tensor'
# Also, assuming we want to split 'sparse_tensor' into 2 tensors along dimension 0

# Create a test sparse tensor
indices = [[0, 0], [1, 0], [2, 0], [3, 0]]
values = [1, 2, 3, 4]
dense_shape = [4, 2]
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Use tf.raw_ops to split sparse tensor dimension-wise
split_op = tf.raw_ops.SparseSplit
split_indices = [0, 1]
output_indices_0 = split_op(sparse_indices=sparse_tensor.indices,
                            sparse_values=sparse_tensor.values,
                            sparse_shape=sparse_tensor.dense_shape,
                            split_dim=0,
                            num_split=2,
                            output_indices=split_indices)

# Results will be a list of SparseTensors
output_values_0 = [tf.SparseTensor(output_indices_0[i],
                                   tf.gather(sparse_tensor.values, output_indices_0[i]),
                                   [tf.shape(output_indices_0[i])[0], sparse_tensor.dense_shape[1]])
                   for i in range(2)]

output_values_0
