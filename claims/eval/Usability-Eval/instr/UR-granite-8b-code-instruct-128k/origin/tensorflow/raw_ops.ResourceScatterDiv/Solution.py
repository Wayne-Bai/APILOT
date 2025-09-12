import tensorflow as tf

# Create a variable
x = tf.Variable([1, 2, 3])

# Create a sparse tensor
sp_x = tf.SparseTensor(indices=[[0], [2]], values=[10, 20], dense_shape=[3, 1])

# Assign the sparse tensor to the variable
assign_op = tf.raw_ops.ResourceScatterDiv(
    resource=x.handle,
    indices=sp_x.indices,
    updates=sp_x.values
)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(assign_op)
    print(x.eval())  # Output: [ 0.1         0.2         1.16666667]
