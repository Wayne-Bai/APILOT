
import tensorflow as tf

# Create a resource variable
var = tf.Variable(0, dtype=tf.int32)

# Create a sparse tensor with values and indices
values = [1, 2, 3]
indices = [[0], [1], [2]]
sparse_update = tf.SparseTensor(indices=indices, values=values, shape=[3])

# Divide the sparse update into the variable
result = var.assign_add(sparse_update)

print(result)
