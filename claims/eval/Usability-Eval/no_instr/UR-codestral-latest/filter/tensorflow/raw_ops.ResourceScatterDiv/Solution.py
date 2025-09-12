import tensorflow as tf

# Define a sparse tensor
indices = [[0, 1], [1, 0]]
values = [1.0, 2.0]
shape = [2, 2]
sp_tensor = tf.SparseTensor(indices, values, shape)

# Define a variable with initial values
var = tf.Variable(tf.constant(2.0, shape=[2, 2], dtype=tf.float32))

# Use tf.raw_ops.SparseApplyDiv, this operation applies sparse updates to the variable.
update = tf.raw_ops.SparseApplyDiv(var=var.handle, indices=sp_tensor.indices, values=sp_tensor.values)

# Initialize variables and run the operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run(update)
    print(result)
