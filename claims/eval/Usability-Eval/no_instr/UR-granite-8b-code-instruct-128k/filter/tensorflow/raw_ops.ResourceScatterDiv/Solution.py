import tensorflow as tf

# Create a variable to hold the state of the variable we want to update
var = tf.Variable([1.0, 2.0, 3.0])

# Create a sparse update to apply to the variable
updates = tf.IndexedSlices(
    values=[0.1, 0.2, 0.3],
    indices=[1, 2, 0],
    dense_shape=[3])

# Create an operation to apply the sparse update to the variable
update_op = tf.raw_ops.ResourceScatterDiv(
    resource=var.handle,
    indices=updates.indices,
    updates=updates.values)

# Initialize the variables and run the update operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(update_op)

# Print the updated variable
print(var.eval())
