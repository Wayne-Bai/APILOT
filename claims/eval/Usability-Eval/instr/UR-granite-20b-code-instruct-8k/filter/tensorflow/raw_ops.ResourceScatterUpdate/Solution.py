import tensorflow as tf

# Define the variable to be updated
variable = tf.Variable([1.0, 2.0, 3.0])

# Define the sparse updates
sparse_updates = tf.IndexedSlices(values=[4.0, 5.0], indices=[1, 2])

# Define the method to assign sparse updates to the variable
assignment = tf.raw_ops.Assign(ref=variable, value=sparse_updates)

# Execute the assignment operation
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(assignment)
    updated_variable = variable.eval()
    print(updated_variable)
